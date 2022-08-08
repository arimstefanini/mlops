from sklearn.metrics import accuracy_score

class Evaluation:

    def get_evaluation(model, X_test, y_test):

        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        
        print(f'LightGBM Model accuracy score: {acc}')

        return y_pred, acc
