# CLI
[![CodeFactor](https://www.codefactor.io/repository/github/gradsflow/cli/badge)](https://www.codefactor.io/repository/github/gradsflow/cli)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/gradsflow/cli/main.svg)](https://results.pre-commit.ci/latest/github/gradsflow/cli/main)

CLI for accessing GradsFlow Codeless AI Engine.

## 📀 Installation

[comment]: <> (### Using pip &#40;recommended&#41;)

[comment]: <> (`pip install -U gflow_cli==0.1.0a0`)

### From source

```
pip install git+https://github.com/gradsflow/cli@master
```

Or,

```
pip install git+https://github.com/gradsflow/cli@master
cd cli
pip install .
```

## 🧑‍💻 Usage

### Setup

Before using the Python Client/CLI you have to set an enviornment variable
`export DEFAULT_ADDR=http://IP:PORT`

For example, if IP=127.0.0.0 and PORT=8080 then set `export DEFAULT_ADDR=http://127.0.0.0:8080`

### Manage Datasets

#### Add Dataset

```
  Usage: gflow dataset add [OPTIONS] PATH TASK DATASET_TYPE REMOTE

  Add Training Dataset
  Args:
      path: Path of dataset on your local filesystem
      task: Type of Task/Model you want to train with this
      dataset. See available tasks `gflow-cli datasets available-tasks`
      dataset_type: `from-folder` or `from-csv`
      remote: if true then dataset will be saved to GradsFlow server

Arguments:
  PATH          [required]
  TASK          [required]
  DATASET_TYPE  [required]
  REMOTE        [required]
```
