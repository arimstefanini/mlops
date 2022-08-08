import argparse
import os
from dotenv import load_dotenv
import json
import logging

from predict.predict_pipeline import PredictPipeline

load_dotenv()

def get_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-d', '--data_file', help='path test dataset', required=True)
    parser.add_argument('-p', '--pickle_config', help='data mlflow model', required=True)
    parser.add_argument('-s', '--submisson', help='folder path data sample submission', required=True)

    return parser.parse_args()

if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)

    """
    exemple args:
        python src/main_predict.py \
            -d data/test_data/test.csv \
            -p src/pickle_config.json \
            -s data/submission_data \
    """
    
    try:

        if os.getenv('ENV_LOCAL') == 'local':
            data_file = os.environ['DATA_FILE']
            pickle_config = os.environ['PICKLE_CONFIG']
            submisson = os.environ['SUBMISSION']

        else:
            args = get_args()

            data_file = args.data_file
            pickle_config = args.pickle_config
            submisson = args.submisson

        f = open(pickle_config)
        config = json.load(f)

        cwd = os.getcwd()
        data_path = f'{cwd}\{data_file}' 
        submission_path = f'{cwd}\{submisson}' 

        predict_pipeline = PredictPipeline()
        predict_pipeline.run(config, data_path, submission_path)

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
   