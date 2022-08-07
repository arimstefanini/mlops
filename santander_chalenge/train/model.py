from lightgbm import LGBMClassifier

class Model:

    def fit_model(X_train, y_train):
        
        clf = LGBMClassifier(
            metric = 'auc',
            objective = 'binary',
            is_unbalance = True,
            learning_rate = 0.005,
            max_bin = 165,
            max_depth = 5,
            min_child_samples = 150,
            min_child_weight = 0.1,
            min_split_gain = 0.0018,
            n_estimators = 41,
            num_leaves = 6,
            verbose = -1,
        )

        clf.fit(X_train, y_train)

        return clf