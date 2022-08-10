from sklearn.metrics import roc_auc_score

class Evaluation:

    def get_evaluation(model, X_test, y_test):

        y_pred = model.predict_proba(X_test)
        auc = roc_auc_score(y_test , y_pred[:,1])
        
        print(f'LightGBM Model AUC score: {auc}')

        return y_pred, auc
