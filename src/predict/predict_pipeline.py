import pickle
import pandas as pd

from mlflow.tracking import MlflowClient

class PredictPipeline:
    
    def run(config, data_path):

        client = MlflowClient()

        tmp_path = client.download_artifacts(run_id=config["run_id"], path=config["path"])

        f = open(tmp_path,'rb')

        model = pickle.load(f)

        test =  pd.read_csv(data_path)
        test = test.drop(columns=['ID_code'])
        a = model.predict(test)

        print(a)