# Serasa Challenge - MLOps project
This repository aims to solve the use case, Santander Customer Transaction Prediction, and deployment using MLOps practices.

# Table of contents
* [Composition](#composition)
    + [Directory](#directory)
* [Getting Started](#getting-started)
  + [Software build](#software-build)
  + [Dependencies](#dependencies)
  + [Docker](#docker)
  + [Local exec](#local-exec)
    + [.env file exec](#env-file-exec)
    + [command line exec](#command-line-exec)

> **_NOTE:_** You can find a problem description of the use case developed in this [link](https://github.com/arimstefanini/serasa-challenge/blob/develop/problem.md)

# Composition

The repository consists of:
   * Train. It fit and saves a model on MLflows.
   * Predict. It runs predicts outcomes using the model.
   * Batch predict. It runs batch predicts.
   * Test. It runs continuous testing.

This program use  [MLflow](https://mlflow.org/) to manage the ML lifecycle, which helps to generate an instant prediction of the LightGBM model for identifying the target.

## Directory
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

# Getting Started
Adopting MLOps practices provides automatization of all the steps in the ML, and with this, we have a faster delivery. And for that, I implemented some technologies to put MLOps into practice.
 
Deploying to [Heroku](https://devcenter.heroku.com/articles/heroku-cli) from [GitHub Acrions](https://github.com/features/actions) 

# Software build
## Dependencies
Dependencies can be installed using this command

`pip install -r requirements.txt`

## Docker 
Command to build and run a docker image

`docker build -t santander-chalange:latest .`

`docker run -it santander-chalange /bin/sh`

or

`docker run -it --env-file .env santander-chalange /bin/sh`


## Local exec
This program has two options for execution, either by .env or by command line passing the parameters by args

### .env file exec

> **_NOTE:_** The program `main_train.py` returns `pickle_config.json`

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

### command line exec
```bash
python src/main_train.py \
    -t [path train dataset]
```
```bash
python src/main_predict.py \
    -d [path test dataset] \
    -p [data mlflow model] \
    -s [folder path data sample submission] \
    -o [folder path output] \
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