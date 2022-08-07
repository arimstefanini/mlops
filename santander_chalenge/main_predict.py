import argparse
import os
from dotenv import load_dotenv
import logging

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

        print(verbose)

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
    
   