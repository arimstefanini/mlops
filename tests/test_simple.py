import pytest
from src.train.ml_pipeline import MLPipeline
from src.train.learning_algorithms.lgbm_evaluator import LGBMEvaluator

EVALUATOR=LGBMEvaluator()

def test_create_pickle_config():
    '''pickle config return a dict'''
    train = MLPipeline(EVALUATOR)
    assert isinstance(train.create_pickle_config("0", "db96a12a47c54af8b46c60e3045026df"), dict)

