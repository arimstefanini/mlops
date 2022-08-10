import pickle
import pandas as pd
import numpy as np
from mlflow.tracking import MlflowClient

class PredictPipeline:

    def run(self, config, data_path, submission_path, output):

        client = MlflowClient()

        tmp_path = client.download_artifacts(run_id=config["run_id"], path=config["path"])

        f = open(tmp_path,'rb')

        model = pickle.load(f)

        test =  pd.read_csv(data_path)
        test = test.drop(columns=['ID_code'])
        
        proba_y = model.predict_proba(test)

        self.create_submission(proba_y, submission_path, output)

    def create_submission(self, proba_y, submission_path, output):

        sample_submission =  pd.read_csv(submission_path)

        y_pred = [ np.where(proba > 0.5)[0][0]  for proba in proba_y ]
        
        my_submission = pd.DataFrame({'ID_code': sample_submission.ID_code, 'target': y_pred})
        my_submission.to_csv(output, index=False)

