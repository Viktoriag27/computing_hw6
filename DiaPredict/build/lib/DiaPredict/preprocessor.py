# preprocessor.py

import pandas as pd
from abc import ABC, abstractmethod

class Preprocessor(ABC):
    @abstractmethod
    def process(self, df):
        pass

class RemoveNaNPreprocessor(Preprocessor):
    def process(self, df):
        # Remove rows with NaN in specified columns
        return df.dropna(subset=['age', 'gender', 'ethnicity'])

class FillNaNPreprocessor(Preprocessor):
    def process(self, df):
        # Fill NaN values with the mean of the column for specified columns
        for column in ['height', 'weight']:
            df[column].fillna(df[column].mean(), inplace=True)
        return df
