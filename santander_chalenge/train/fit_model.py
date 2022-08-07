from lightgbm import LGBMClassifier

class FitModel:

    def fit_model(clf, X_train, y_train):
        
        clf.fit(X_train, y_train)

        return clf