import os
import json
import argparse
from dotenv import load_dotenv
import logging
import multiprocessing

from predict.predict_pipeline import PredictPipeline

load_dotenv()

def get_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-d', '--data_file', nargs='+', default=[], help='path test dataset split by space', required=True)

    return parser.parse_args()

if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)

    """
    exemple args:
        python src/main_batch_pred.py \
            -d test test_copy test_copy2 \
    """
    
    try:

        if os.getenv('ENV_LOCAL') == 'local':
            
            data_files = os.environ['DATA_FILES']
            data_files = data_files.split(",")

        else:
            args = get_args()

            data_files = args.data_file

        procs = []
        cwd = os.getcwd()
        pickle_config = 'src/pickle_config.json'
        sample_submission =  f'{cwd}/data/submission_data/sample_submission.csv'

        f = open(pickle_config)
        config = json.load(f)

        ##
        # PREDICT PIPELINE PARALLEL PROCESSING
        ##

        logging.debug("Start predict pipeline in bach")

        predict_pipeline = PredictPipeline()

        pool = multiprocessing.Pool(processes=3)
        for data in data_files:
            output = f'{cwd}/data/submission_data/submission_{data}.csv'
            pool.apply_async(predict_pipeline.run, args=(config, f'{cwd}/data/test_data/{data}.csv', sample_submission, output,))

        pool.close()
        pool.join()
        logging.debug("Finish predict pipeline in bach")

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
   