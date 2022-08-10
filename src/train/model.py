from lightgbm import LGBMClassifier

class Model:

    def fit_model(clf, X_train, y_train):
        
        clf.fit(X_train, y_train)

        return clf