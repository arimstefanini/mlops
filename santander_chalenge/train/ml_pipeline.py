from train.repositories.evaluator_repository import Evaluator

from train.build_dataset import BuildDataset
from train.model import Model
from train.evaluation import Evaluation

import mlflow
from mlflow.models.signature import infer_signature

mlflow.set_experiment('santander_chalenge')
mlflow.lightgbm.autolog()
class MLPipeline():

    def __init__(self, evaluator: Evaluator):
        self.evaluator = evaluator

    def run(self, data_path):
        
        with mlflow.start_run(run_name="lgbm_model"):

            X_train, X_test, y_train, y_test = BuildDataset.split_data(data_path)
            
            model = self.evaluator.evaluate()
            Model.fit_model(model, X_train, y_train)

            y_pred, acc = Evaluation.get_evaluation(model, X_test, y_test)


            mlflow.log_metric("accuracy", acc)
            signature = infer_signature(X_train, y_pred)
            mlflow.lightgbm.log_model(model, "model", signature=signature)

        mlflow.end_run()
