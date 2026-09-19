"""Split extracted DOCX chat archives into deduplicated prompt/response records.

Speaker labels are not present in the source DOCX extraction. Boundaries are therefore
heuristic and every generated record is marked INFERRED_BOUNDARY.
"""

from __future__ import annotations

import hashlib
import re
import shutil
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
M = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"


def linearize(elem):
    out = []

    def walk(node):
        tag = node.tag
        if tag in (W + "t", M + "t"):
            out.append(node.text or "")
        elif tag in (W + "tab",):
            out.append("\t")
        elif tag in (W + "br", W + "cr"):
            out.append("\n")
        elif tag == W + "p":
            for child in node:
                walk(child)
            out.append("\n")
        elif tag == M + "oMath" or tag == M + "oMathPara":
            out.append(" [EQ: ")
            for child in node:
                walk(child)
            out.append(" ] ")
        elif tag == M + "f":
            num = node.find(M + "num")
            den = node.find(M + "den")
            out.append("(")
            if num is not None:
                for child in num:
                    walk(child)
            out.append(")/(")
            if den is not None:
                for child in den:
                    walk(child)
            out.append(")")
        elif tag == M + "sSup":
            base = node.find(M + "e")
            sup = node.find(M + "sup")
            if base is not None:
                for child in base:
                    walk(child)
            out.append("^(")
            if sup is not None:
                for child in sup:
                    walk(child)
            out.append(")")
        elif tag == M + "sSub":
            base = node.find(M + "e")
            sub = node.find(M + "sub")
            if base is not None:
                for child in base:
                    walk(child)
            out.append("_(")
            if sub is not None:
                for child in sub:
                    walk(child)
            out.append(")")
        else:
            for child in node:
                walk(child)

    walk(elem)
    return "".join(out)


def extract_docx(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    body = root.find(W + "body")
    text = linearize(body)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold()


def looks_like_prompt(paragraph: str) -> bool:
    text = paragraph.strip()
    if not text or len(text) > 1400:
        return False
    lower = text.casefold()
    # Reject common assistant-side section headings before looking for prompt openings.
    if re.match(r"^(?:\d+|[a-j])\.\s", lower):
        return False
    if re.match(r"^(?:pga[- ]?\d+|test\s+\d+|level\s+\d+|step\s+\d+|axiom\s+\d+|law\s+\d+|outcome\s+\d+|chapter\s+\d+)\b", lower):
        return False
    if lower.startswith((
        "yes.", "the ", "this ", "that ", "now ", "and ", "but ", "so ",
        "therefore ", "important ", "result ", "interpretation ", "decision ",
        "next ", "current ", "we ", "you ", "it ", "suppose ", "imagine ",
        "consider ", "for example", "in other words", "one important", "another ",
        "a ", "an ", "if ", "when ", "for ", "at ", "let ", "take ", "use ",
        "start with ", "introduce ", "define ", "apply ", "look at ", "here ",
    )):
        return False
    if lower in {"pga", "ok pga", "pga proceed", "yes", "please proceed"}:
        return True
    cue = re.match(
        r"^(well\b|i think\b|i want\b|i would\b|i feel\b|i believe\b|can you\b|can u\b|could you\b|please\b|pls\b|"
        r"what\b|why\b|how\b|is there\b|are there\b|do we\b|does\b|would\b|should\b|"
        r"let us\b|let's\b|ok\b|run\b|build\b|test\b|create\b|extract\b|proceed\b|continue\b|pga\b|"
        r"did we\b|can we\b|now can\b|so what\b|hope\b|also\b)", lower
    )
    question = "?" in text and bool(re.match(r"^(can|could|what|why|how|is|are|do|does|would|should)\b", lower))
    imperative = bool(re.search(r"\b(run|build|test|create|check|extract|proceed|continue)\b", lower)) and len(text) < 500
    return bool(cue or (question and len(text) < 700) or imperative)


def split_paragraphs(text: str):
    return [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]


def split_turns(text: str):
    paragraphs = split_paragraphs(text)
    starts = [index for index, paragraph in enumerate(paragraphs) if looks_like_prompt(paragraph)]
    if not starts:
        return []
    turns = []
    for position, start in enumerate(starts):
        end = starts[position + 1] if position + 1 < len(starts) else len(paragraphs)
        prompt = paragraphs[start]
        response = "\n\n".join(paragraphs[start + 1:end]).strip()
        if response:
            turns.append((prompt, response))
    return turns


def slug(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", text.casefold()).strip("-")
    return value[:60] or "untitled"


def record_key(prompt: str, response: str) -> str:
    payload = normalize(prompt) + "\n" + normalize(response)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: split_chat_archives.py SOURCE_CHAT_DIR OUTPUT_DIR")
    source_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    source_order = {
        "ChatGPT - Indian Philosophy and Modern Physics -11Sep26.docx": 1,
        "Indian Philosophy and Modern Physics - AI and Standard Model.docx": 2,
        "Indian Philosophy and Modern Physics - Branch · Assess Research Pattern.docx": 3,
        "Indian Philosophy and Modern Physics - Branch · Summarize Philosophy Physics Project.docx": 4,
        "Indian Philosophy and Modern Physics - Recreate Gravity Diagram.docx": 5,
    }
    source_files = sorted(source_dir.glob("*.docx"), key=lambda path: source_order.get(path.name, 99))
    seen = set()
    records = []
    for source in source_files:
        text = extract_docx(source)
        for local_index, (prompt, response) in enumerate(split_turns(text), start=1):
            key = record_key(prompt, response)
            if key in seen:
                continue
            seen.add(key)
            records.append({
                "source": source.name,
                "source_sequence": local_index,
                "prompt": prompt,
                "response": response,
                "key": key,
            })

    index_lines = [
        "# Split Chat Archive",
        "",
        "This directory contains one conservative, inferred prompt/model-response pair per Markdown file.",
        "",
        "**Boundary status:** `INFERRED_BOUNDARY`. The source DOCX files do not expose reliable speaker metadata; prompts were identified only at strong conversational cues, while numbered sections and assistant-style continuation headings are kept inside the preceding response. Review records before treating boundaries as authoritative.",
        "",
        "**Deduplication:** exact normalized prompt-response duplicates were removed, keeping the first source occurrence.",
        "",
        "| File | Source | Source sequence | Prompt preview |",
        "|---|---|---:|---|",
    ]
    for sequence, record in enumerate(records, start=1):
        filename = f"CHAT_{sequence:04d}_{slug(record['prompt'])}.md"
        content = "\n".join([
            f"# Chat {sequence:04d} - {record['prompt'][:100]}",
            "",
            "**Boundary status:** `INFERRED_BOUNDARY`",
            f"**Source DOCX:** `{record['source']}`",
            f"**Source sequence:** `{record['source_sequence']}`",
            f"**Deduplication key:** `{record['key']}`",
            "",
            "## Prompt",
            "",
            record["prompt"],
            "",
            "## Model response",
            "",
            record["response"],
            "",
            "## Provenance note",
            "",
            "This record was split from the immutable DOCX archive. Equations use the repository's linearized `[EQ: ... ]` form. The prompt/response boundary is inferred and should be audited before scientific use.",
            "",
        ])
        (output_dir / filename).write_text(content, encoding="utf-8")
        preview = re.sub(r"\s+", " ", record["prompt"]).replace("|", "\\|")[:100]
        index_lines.append(f"| [{filename}]({filename}) | `{record['source']}` | {record['source_sequence']} | {preview} |")
    (output_dir / "INDEX.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    (output_dir / "README.md").write_text(
        "# Split Chat Archive\n\n"
        "Generated from the five DOCX files in `indian-philosophy-modern-physics/V3/chats/`. "
        "Each file contains one conservative, inferred prompt and its following model response. Exact normalized duplicates are omitted.\n\n"
        "The source DOCX files remain unchanged. Because speaker metadata was not available in the extracted document structure, every record is labeled `INFERRED_BOUNDARY` and should be reviewed before being treated as an authoritative transcript.\n",
        encoding="utf-8",
    )
    print(f"sources={len(source_files)} records={len(records)} output={output_dir}")


if __name__ == "__main__":
    main()
