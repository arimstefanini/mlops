import pytest
import pandas as pd

from src.train.ml_pipeline import MLPipeline
from src.train.learning_algorithms.lgbm_evaluator import LGBMEvaluator
from src.train.build_dataset import BuildDataset

EVALUATOR=LGBMEvaluator()
  
def test_valid_data():
    '''pickle config return a dict'''
    build_data = BuildDataset()  

    data_mock = {'ID_code':['train_0','train_1','train_2'],
            'target':[0,0,0],
            'var_0':[8.9255,11.5006,8.6093]}

    train_data = pd.DataFrame(data_mock)

    assert build_data.validate_data(train_data) == True

def test_invalid_data():
    '''pickle config return a dict'''
    build_data = BuildDataset()  

    data_mock = {'ID_code':['train_0','train_0','train_2'],
            'target':[0,0,0],
            'var_0':[8.9255,11.5006,8.6093]}

    train_data = pd.DataFrame(data_mock)

    assert build_data.validate_data(train_data) == False

def test_create_pickle_config():
    '''pickle config return a dict'''
    train = MLPipeline(EVALUATOR)   
    assert isinstance(train.create_pickle_config("0", "db96a12a47c54af8b46c60e3045026df"), dict)