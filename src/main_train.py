import argparse
import os
from dotenv import load_dotenv
import logging

from train.learning_algorithms.lgbm_evaluator import LGBMEvaluator
from train.ml_pipeline import MLPipeline

load_dotenv()

def get_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-t', '--train_file', help='path train dataset', required=True)

    return parser.parse_args()

if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)
    
    """
    exemple exec:
        python src/main_train.py \
            -t data/train_data/train.csv 
    """

    try:

        if os.getenv('ENV_LOCAL') == 'local':
            train_file = os.environ['TRAIN_FILE']

        else:
            args = get_args()

            train_file = args.train_file

        cwd = os.getcwd()

        data_path = f'{cwd}/{train_file}'

        ##
        # ML PIPELINE
        ##

        logging.debug("Start ml pipeline")

        evaluator = LGBMEvaluator()
        ml_pipeline = MLPipeline(evaluator)
        ml_pipeline.run(data_path)

        logging.debug("Finish ml pipeline")

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
    
   