import argparse
import os
from dotenv import load_dotenv
import logging

from train.learning_algorithms.lgbm_evaluator import LGBMEvaluator
from train.ml_pipeline import MLPipeline

load_dotenv()

def get_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-d', '--data_file', help='an optional argument', required=True)

    return parser.parse_args()

if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)
    
    """
    exemple args:
        python santander_chalenge/main_train.py -d /data/train_data/train.csv 
    """

    try:

        if os.getenv('ENV_LOCAL') == 'local':
            data_file = os.environ['data_file']

        else:
            args = get_args()

            data_file = args.data_file

        cwd = os.getcwd()

        data_path = f'{cwd}\{data_file}'

        evaluator = LGBMEvaluator()
        ml_pipeline = MLPipeline(evaluator)
        ml_pipeline.run(data_path)

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
    
   