from pytest import raises
from src.train.ml_pipeline import MLPipeline
from src.train.learning_algorithms.lgbm_evaluator import LGBMEvaluator

EVALUATOR=LGBMEvaluator()

class SimpleTest:

    def setup(self):
        self.eval = MLPipeline(EVALUATOR)

    def test_create_pickle_config(self):
        '''pickle config return a dict'''
        assert isinstance(self.eval.create_pickle_config("0", "db96a12a47c54af8b46c60e3045026df"), dict)

    def test_empty_pickle_config(self):
        '''pickle config params is empty'''
        assert self.eval.create_pickle_config("", "") == False
