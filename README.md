# Serasa Challenge - MLOps project
This project is about a struct apply ML to build a production grade product to deliver value with good practices of MLOps

# Table of contents
* [Overview](#overview)
* [Getting Started](#getting-started)
  + [Installation](#installation)
  + [Docker](#docker)
* [Exectution the Project](#exectution-the-project)
  + [Env file exec](#env-file-exec)
  + [Args exec](#args-exec)
    + [Warning](#warning)

# Overview

> **_NOTE:_** You can find a little more about the problem developed in this [link](https://github.com/arimstefanini/serasa-challenge/blob/develop/problem.md)

COLOCAR UM DIAGRAMA

This code was implemented using  [MLflow](https://mlflow.org/) to manage the ML lifecycle.
To meet MLOps practices, the system was developed with [Argo Workflow](https://argoproj.github.io/argo-workflows/) which helps to generate an instant predict of the lgbm model for identify who make a transaction.

# Getting Started
I focus on the fundamentals and then dive into the code, at which point we can refer to this repository as a guide. 
## Installation Dependences
Dependencies can be installed using this command

`pip install -r requirements.txt`

### Directory
```
serasa-challenge/
|-- src/
|    |-- predict/                                  
     |-- train/
     |-- main_batch_pred.py        - inference in batch files utilities
     |-- main_predict.py           - inference utilities
     |-- main_train.py             - training/optimization operations
|-- tests/
     |-- test_simple.py            - test unit with pytest
```

## Docker
Command to build and run a docker image

`docker build -t santander-chalange:latest .`

`docker run -it santander-chalange /bin/sh`

or

`docker run -it --env-file .env santander-chalange /bin/sh`


# Workflow
This program has two options for execution, either by .env or by command line passing the parameters by args
## .env file exec
> **_NOTE:_** The file `main_train.py` returns `pickle_config.json`

`python src/main_train.py`

`python src/main_predict.py`

or

`python src/main_batch_pred.py`

If you want to use .env, here's an example for the file
```t
ENV_LOCAL=local

# env main_train
TRAIN_FILE=data/train_data/train.csv

# env main_predict
DATA_FILE=data/test_data/test.csv
PICKLE_CONFIG=src/pickle_config.json
SUBMISSION=data/submission_data/sample_submission.csv
OUTPUT=data/submission_data/submission.csv

# env main_pred_bach
DATA_FILES=test,test_copy,test_copy2
```

## command line exec
```bash
python src/main_train.py \
    -t [path train dataset]
```
```bash
python src/main_predict.py \
    -d [path test dataset] \
    -p [data mlflow model] \
    -s [folder path data sample submission] \
    -s [folder path output] \
```
or
```bash
python src/main_batch_pred.py \
    -d [name files test dataset split by single space]
```

> **_Warning:_** 
The predict needs to `piclek_config.json` to execturion with MLflow data. 

Here is an example file.
```json
{
    "experiment_id": [experimet name],
    "run_id": [run id code],
    "path": [path model.pkl]
}
```