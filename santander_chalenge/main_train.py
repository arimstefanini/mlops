import argparse
import os
from dotenv import load_dotenv
import logging

from train.build_dataset import BuildDataset
from train.model import Model
from train.evaluation import Evaluation

load_dotenv()

def get_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-d', '--file_data', help='an optional argument', required=True)

    return parser.parse_args()

if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)

    """
    exemple args:
        python santander_chalenge/main_train.py -d data/train_data/train.csv 
    """

    try:

        if os.getenv('ENV_LOCAL') == 'local':
            file_data = os.environ['file_data']

        else:
            args = get_args()

            file_data = args.file_data

        cwd = os.getcwd()

        X_train, X_test, y_train, y_test = BuildDataset.split_data(f'{cwd}/{file_data}')

        model = Model.fit_model(X_train, y_train)

        Evaluation.get_evaluation(model, X_test, y_test)

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
    
   