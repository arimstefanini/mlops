from lightgbm import LGBMClassifier

from train.repositories.evaluator_repository import Evaluator
class LGBMEvaluator(Evaluator):
    
    def evaluate(self):
        clf = LGBMClassifier(
                metric = 'auc',
                objective = 'binary',
                is_unbalance = True,
                n_jobs = -1, 
                verbose = -1,
                learning_rate = 0.05,
                max_bin = 165,
                max_depth = 5,
                min_child_samples = 150,
                min_child_weight = 0.1,
                min_split_gain = 0.0018,
                n_estimators = 41,
                num_leaves = 6,
                reg_alpha = 2.0,
                reg_lambda = 2.54,
        )

        return clf