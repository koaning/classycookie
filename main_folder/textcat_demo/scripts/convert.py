"""Convert textcat annotation from JSONL to spaCy v3 .spacy format."""
import srsly
import typer
from clumper import Clumper
from pathlib import Path
from rich.console import Console

import spacy
from spacy.tokens import DocBin


def convert(lang: str, input_path: Path, output_path: Path):
    nlp = spacy.blank(lang)
    console = Console()
    c = Clumper.read_jsonl(input_path)
    classes = {k: 0 for k in c.unique("label")}

    db = DocBin()
    for line in srsly.read_jsonl(input_path):
        doc = nlp.make_doc(line["text"])
        doc.cats = {**classes, **{line["label"]: 1}}
        db.add(doc)
    db.to_disk(output_path)
    console.log(f"spacy file written at {output_path}")

if __name__ == "__main__":
    typer.run(convert)
