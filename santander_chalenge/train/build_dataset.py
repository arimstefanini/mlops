import pandas as pd

from sklearn.model_selection import train_test_split

class BuildDataset:
    
    def split_data(file):

        data =  pd.read_csv(file)
        
        train = data.drop(columns=['ID_code'])

        feat = train.drop(columns=['target'])
        label = train['target']

        return train_test_split(feat, label, test_size = 0.3, random_state = 17, shuffle=True)
