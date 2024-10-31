# model.py

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

class Model:
    def __init__(self, feature_columns, target_column, model_type='logistic', hyperparameters=None):
        self.feature_columns = feature_columns
        self.target_column = target_column
        self.model_type = model_type
        self.hyperparameters = hyperparameters or {}
        self.model = self._initialize_model()

    def _initialize_model(self):
        if self.model_type == 'logistic':
            return LogisticRegression(**self.hyperparameters)
        elif self.model_type == 'random_forest':
            return RandomForestClassifier(**self.hyperparameters)
        else:
            raise ValueError("Unsupported model type.")

    def train(self, train_df):
        X_train = train_df[self.feature_columns]
        y_train = train_df[self.target_column]
        self.model.fit(X_train, y_train)

    def predict(self, test_df):
        X_test = test_df[self.feature_columns]
        return self.model.predict_proba(X_test)[:, 1]  # Return probabilities for the positive class
