# feature_extraction.py

import pandas as pd
from abc import ABC, abstractmethod

class FeatureTransformer(ABC):
    @abstractmethod
    def transform(self, df):
        pass

class FeatureTransformer1(FeatureTransformer):
    def transform(self, df):
        # Example transformation: Create a new feature from existing ones
        df['age_squared'] = df['age'] ** 2
        return df

class FeatureTransformer2(FeatureTransformer):
    def transform(self, df):
        # Example transformation: Normalize a feature
        df['height_normalized'] = (df['height'] - df['height'].mean()) / df['height'].std()
        return df
