from train.repositories.evaluator import Evaluator

from train.build_dataset import BuildDataset
from train.evaluation import Evaluation

class MLPipeline():

    def __init__(self, evaluator: Evaluator):
        self.evaluator = evaluator

    def evaluator(self, data_path):

        X_train, X_test, y_train, y_test = BuildDataset.split_data(data_path)

        model = self.evaluator.evaluate(X_train, y_train)

        Evaluation.get_evaluation(model, X_test, y_test)