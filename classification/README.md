<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Basic Text Classification Benchmarks

Text classification benchmarks with scikit-learn and spaCy v3.

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `prepare` | Prepare the .csv for the next steps |
| `convert` | Convert the data to spaCy's binary format |
| `train-spacy` | Train the spaCy models |
| `train-sklearn` | Train the spaCy models |
| `evaluate` | Evaluate the model and export metrics |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `prepare` &rarr; `convert` &rarr; `train-spacy` &rarr; `train-sklearn` &rarr; `evaluate` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| [`assets/data.csv`](assets/data.csv) | Local | Original `.csv` file. |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
