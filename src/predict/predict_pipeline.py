import pickle
import pandas as pd

from mlflow.tracking import MlflowClient

class PredictPipeline:

    def run(self, config, data_path, submission_path, output):

        client = MlflowClient()

        tmp_path = client.download_artifacts(run_id=config["run_id"], path=config["path"])

        f = open(tmp_path,'rb')

        model = pickle.load(f)

        test =  pd.read_csv(data_path)
        test = test.drop(columns=['ID_code'])
        predict_santander = model.predict(test)

        self.create_submission(predict_santander, submission_path, output)

    def create_submission(self, predict_santander, submission_path, output):

        sample_submission =  pd.read_csv(submission_path)
        sample_submission = pd.DataFrame(sample_submission)
        
        my_submission = pd.DataFrame({'ID_code': sample_submission.ID_code, 'target': predict_santander})
        my_submission.to_csv(output, index=False)

