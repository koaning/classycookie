<img src="cookie.png" width="150" height="150" align="right" />

# 🪐 spaCy Project: classycookie

Text classification benchmarks with scikit-learn and spaCy v3.

This project assumes that there is a `data.csv` file in the `assets` folder
that contains data for a basic text classification task. This
file needs to have one column named `"text"` and another one named `"label"`. 
It can also contain an optional column called `"set"` which can contain
either the value `"valid"` and `"train"`. If this column is missing this project
will make a random 50% split.

This data will be modelled in four different ways. 

1. a spaCy bag of words model. 
2. a spaCy CNN model. 
3. a scikit-learn countvectorizer logistic classifier
4. a scikit-learn tf/idf logistic classifier

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

This project comes with a copy of the [clinc dataset](https://github.com/clinc/oos-eval) that you can replace at will. 

### End Result 

The final result of the project will be a summary table like this one:

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃ Model                      ┃ Train Score ┃ Valid Score ┃ Time Taken          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ sklearn-trained/pipe_tfid… │ 0.9262      │ 0.8582      │ 0.15783333778381348 │
│ sklearn-trained/pipe_cv.j… │ 0.9866      │ 0.8955      │ 0.14619827270507812 │
│ training/cnn/model-best    │ 0.9867      │ 0.8723      │ 3.962278127670288   │
│ training/bow/model-best    │ 0.9867      │ 0.8723      │ 4.037751197814941   │
└────────────────────────────┴─────────────┴─────────────┴─────────────────────┘
```

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
