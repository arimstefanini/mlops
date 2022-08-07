import pandas as pd

from sklearn.model_selection import train_test_split

class BuildDataset:
    
    def split_data(file):
        print(file)
        data =  pd.read_csv(file)
        
        train = data.drop(columns=['ID_code'])

        feat = train.drop(columns=['target'])
        label = train['target']

        #(x_train, y_train), (x_test, y_test) = get_metadata(random_state=random_state)

        return train_test_split(feat, label, test_size = 0.3, random_state = 17, shuffle=True)
