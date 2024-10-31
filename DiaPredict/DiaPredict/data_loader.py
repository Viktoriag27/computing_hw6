# data_loader.py

import pandas as pd
from sklearn.model_selection import train_test_split

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        # Load the dataset and split into train and test
        df = pd.read_csv(self.file_path)
        train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
        return train_df, test_df
