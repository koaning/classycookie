"""Prepare files for ML steps. Converts the CSV file."""
import typer
import random 
import pathlib
from rich.console import Console
from clumper import Clumper
from pathlib import Path


def prepare(input_path: Path, train_jsonl: Path, valid_jsonl: Path):
    random.seed(42)
    console = Console()
    clump = (Clumper.read_csv(input_path)
      .mutate(set=lambda d: "valid" if random.random() < 0.5 else "train")
      .select("text", "label", "set"))
    
    if pathlib.Path(train_jsonl).exists():
        pathlib.Path(train_jsonl).unlink()
    clump.keep(lambda d: d["set"] == "train").write_jsonl(train_jsonl)
    console.log(f"train jsonl file written at {train_jsonl}")

    if pathlib.Path(valid_jsonl).exists():
        pathlib.Path(valid_jsonl).unlink()
    clump.keep(lambda d: d["set"] == "valid").write_jsonl(valid_jsonl)
    console.log(f"train jsonl file written at {valid_jsonl}")

if __name__ == "__main__":
    typer.run(prepare)
