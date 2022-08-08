import json
import logging
from train.repositories.evaluator_repository import Evaluator
from train.build_dataset import BuildDataset
from train.model import Model
from train.evaluation import Evaluation

import mlflow
from mlflow.models.signature import infer_signature

experiment_name = 'santander_chalenge'
mlflow.set_experiment(experiment_name)
mlflow.lightgbm.autolog()

class MLPipeline():

    def __init__(self, evaluator: Evaluator):
        self.evaluator = evaluator

    def run(self, data_path):

        buid_dataset = BuildDataset()
        X_train, X_test, y_train, y_test = buid_dataset.split_data(data_path)

        with mlflow.start_run(run_name="lgbm_model"):
            
            model = self.evaluator.evaluate()
            Model.fit_model(model, X_train, y_train)

            y_pred, acc = Evaluation.get_evaluation(model, X_test, y_test)

            mlflow.log_metric("accuracy", acc)
            signature = infer_signature(X_train, y_pred)
            mlflow.lightgbm.log_model(model, "model", signature=signature)

            current_experiment=dict(mlflow.get_experiment_by_name(experiment_name))
            experiment_id = current_experiment['experiment_id']
            df = mlflow.search_runs([experiment_id], order_by=["metrics.accuracy DESC"])
            best_run_id = df.loc[0,'run_id']

            self.create_pickle_config(experiment_id, best_run_id)

        mlflow.end_run()

    def create_pickle_config(self, experiment_id, best_run_id):
  
        if experiment_id != "" and best_run_id != "":
            pickle_config = {"experiment_id":experiment_id,"run_id":best_run_id, "path":'model/model.pkl'}
            with open('./src/pickle_config.json', 'w') as f:
                json.dump(pickle_config, f, ensure_ascii=False, indent=4)
        return pickle_config
