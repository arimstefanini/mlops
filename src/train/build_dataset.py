import pandas as pd
import great_expectations as ge

from sklearn.model_selection import train_test_split

class BuildDataset:
    
    def split_data(self, file):

        data =  pd.read_csv(file)

        valid = self.validate_data(data)
        
        if valid:
            train_data = data.drop(columns=['ID_code'])

            feat = train_data.drop(columns=['target'])
            label = train_data['target']

            return train_test_split(feat, label, test_size = 0.3, random_state = 17, shuffle=True)

        else:
            raise Exception("Dataset is invalid")

    def validate_data(self, train_data):

        df = ge.dataset.PandasDataset(train_data)

        df.expect_compound_columns_to_be_unique(column_list = ["ID_code"])
        df.expect_column_values_to_not_be_null(column = "target")
        df.expect_column_values_to_be_of_type(column = "var_0", type_ = "float64")

        expectation_suite = df.get_expectation_suite(discard_failed_expectations=False)
        valid = df.validate(expectation_suite=expectation_suite, only_return_failures=True)
        
        return valid.get('success')