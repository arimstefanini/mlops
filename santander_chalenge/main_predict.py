import argparse
import os
from dotenv import load_dotenv
import logging
import pickle
import pandas as pd
from mlflow.tracking import MlflowClient

load_dotenv()

def get_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-v', '--verbose', help='an optional argument', required=True)

    return parser.parse_args()

if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)

    """
    exemple args:
        python santander_chalenge/main_train.py -d data/train_data/train.csv 
    """
    
    try:

        if os.getenv('ENV_LOCAL') == 'local':
            verbose = os.environ['VERBOSE']

        else:
            args = get_args()

            verbose = args.verbose


        client = MlflowClient()

        tmp_path = client.download_artifacts(run_id="995b4131b4364d33860c645d37316e4d", path='model/model.pkl')

        f = open(tmp_path,'rb')

        model = pickle.load(f)

        test =  pd.read_csv('C:\\Users\\arist\\OneDrive\\Documentos\\GitHub\\serasa-challenge\\data\\test_data\\test.csv')
        test = test.drop(columns=['ID_code'])
        a = model.predict(test)

        print(a)

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
   