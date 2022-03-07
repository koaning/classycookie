import time 
import typer
import spacy
import numpy as np
from joblib import load
from pathlib import Path
from clumper import Clumper 
from rich.console import Console
from rich.table import Table


console = Console()

def select_argmax(d):
    for k, v in d.items():
        if v == max(d.values()):
            return k

def main(valid_data: Path, train_data: Path):
    sklearn_models = Path("sklearn-trained").glob("*.joblib")
    c = Clumper.read_jsonl(train_data).collect()
    X_train = [_["text"] for _ in c]
    y_train = [_["label"] for _ in c]
    
    c = Clumper.read_jsonl(valid_data).collect()
    X_valid = [_["text"] for _ in c]
    y_valid = [_["label"] for _ in c]

    table = Table(title="Performance Numbers")
    table.add_column("Model", style="cyan")
    table.add_column("Train Score", justify="left", style="magenta")
    table.add_column("Valid Score", justify="left", style="magenta")
    table.add_column("Time Taken", justify="left", style="magenta")

    for mod in sklearn_models:
        pipe = load(mod)
        t0 = time.time()
        preds_valid = pipe.predict(X_valid)
        preds_train = pipe.predict(X_train)
        t1 = time.time()
        table.add_row(
            str(mod), 
            str(np.round(np.mean([a == b for a,b in zip(preds_train, y_train)]), 4)),
            str(np.round(np.mean([a == b for a,b in zip(preds_valid, y_valid)]), 4)),
            str(t1 - t0)
        )
    
    spacy_models = Path("training").glob("*/model-best")
    for mod in spacy_models:
        nlp = spacy.load(mod)
        t0 = time.time()
        list(nlp.pipe(X_valid))
        list(nlp.pipe(X_train))
        t1 = time.time()
        preds_train = [select_argmax(d.cats) for d in nlp.pipe(X_train)]
        preds_valid = [select_argmax(d.cats) for d in nlp.pipe(X_valid)]
        table.add_row(
            str(mod), 
            str(np.round(np.mean([a == b for a,b in zip(preds_train, y_train)]), 4)),
            str(np.round(np.mean([a == b for a,b in zip(preds_valid, y_valid)]), 4)),
            str(t1 - t0)
        )
    
    console.print(table)

if __name__ == "__main__":
    try:
        typer.run(main)
    except SystemExit:
        pass
