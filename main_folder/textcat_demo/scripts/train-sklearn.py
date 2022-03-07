import typer
from joblib import dump
from clumper import Clumper
from pathlib import Path

from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from rich.console import Console

def train_sklearn(train_jsonl: Path, out: Path, kind: str):
    console = Console()
    if kind == "cv":
        pipe = make_pipeline(CountVectorizer(), LogisticRegression())
    elif kind =="tfidf":
        pipe = make_pipeline(TfidfVectorizer(), LogisticRegression())
    else:
        raise ValueError("Kind must be `cv` or `tfidf`.")

    train_set = Clumper.read_jsonl(train_jsonl).collect()
    X = [_["text"] for _ in train_set]
    y = [_["label"] for _ in train_set]
    console.log("Data has been read.")

    pipe.fit(X, y)
    console.log(f"Model kind={kind} trained.")
    path_out = Path(out, f'pipe_{kind}.joblib')
    dump(pipe, str(path_out))
    console.log(f"Joblib pickle saved at {path_out}.")

if __name__ == "__main__":
    typer.run(train_sklearn)
