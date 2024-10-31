# model.py
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import numpy as np

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

        # Check the distribution of classes
        class_distribution = y_train.value_counts()
        print(f"Class distribution in training data:\n{class_distribution}")

        # Check if we have both classes
        if len(class_distribution) < 2:
            print("Warning: Training data contains only one class. Model training will be skipped.")
            return  # Skip training

        self.model.fit(X_train, y_train)

    def predict(self, test_df):
        if not hasattr(self.model, 'coef_'):  # Check if the model has been fitted
            print("Model has not been trained. Returning default predictions.")
            return np.zeros(test_df.shape[0])  # Return an array of zeros or np.nan
        
        X_test = test_df[self.feature_columns]
        return self.model.predict_proba(X_test)[:, 1]  # Return probabilities for the positive class



# from sklearn.linear_model import LogisticRegression
# from sklearn.ensemble import RandomForestClassifier

# class Model:
#     def __init__(self, feature_columns, target_column, model_type='logistic', hyperparameters=None):
#         self.feature_columns = feature_columns
#         self.target_column = target_column
#         self.model_type = model_type
#         self.hyperparameters = hyperparameters or {}
#         self.model = self._initialize_model()

#     def _initialize_model(self):
#         if self.model_type == 'logistic':
#             return LogisticRegression(**self.hyperparameters)
#         elif self.model_type == 'random_forest':
#             return RandomForestClassifier(**self.hyperparameters)
#         else:
#             raise ValueError("Unsupported model type.")

#     def train(self, train_df):
#         X_train = train_df[self.feature_columns]
#         y_train = train_df[self.target_column]
#         self.model.fit(X_train, y_train)

#     def predict(self, test_df):
#         X_test = test_df[self.feature_columns]
#         return self.model.predict_proba(X_test)[:, 1]  # Return probabilities for the positive class
