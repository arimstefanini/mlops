from sklearn.metrics import accuracy_score

class Evaluation:

    def get_evaluation(model, X_test, y_test):

        y_pred = model.predict(X_test)

        print('LightGBM Model accuracy score: {0:0.4f}'.format(accuracy_score(y_test, y_pred)))
