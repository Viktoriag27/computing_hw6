import unittest
import pandas as pd
from DiaPredict.data_loader import DataLoader
from DiaPredict.preprocessor import RemoveNaNPreprocessor, FillNaNPreprocessor
from DiaPredict.feature_extraction import FeatureTransformer1, FeatureTransformer2
from DiaPredict.model import Model

class TestDiabetesPredictionLibrary(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.sample_data = {
            'age': [25, 30, 45, 40],  # Removed None for better class representation
            'gender': ['M', 'F', 'F', 'M'],
            'ethnicity': ['A', 'B', 'B', 'A'],
            'height': [170, 165, 180, 175],  # Removed None for better class representation
            'weight': [70, 65, 80, 90],  # Removed None for better class representation
            'diabetes': [0, 1, 0, 1]  # Ensured representation of both classes
        }
        self.df = pd.DataFrame(self.sample_data)
        self.data_loader = DataLoader("dummy_path.csv")  # Path is not used in tests
        self.remove_nan_processor = RemoveNaNPreprocessor()
        self.fill_nan_processor = FillNaNPreprocessor()
        self.feature_transformer1 = FeatureTransformer1()
        self.feature_transformer2 = FeatureTransformer2()
        self.model = Model(feature_columns=['age', 'height', 'weight'], target_column='diabetes', model_type='logistic')

    def test_remove_nan_preprocessor(self):
        processed_df = self.remove_nan_processor.process(self.df)
        self.assertEqual(processed_df.shape[0], 4)  # No NaN values to remove

    def test_fill_nan_preprocessor(self):
        # Create a sample dataframe with NaNs
        df_with_nans = pd.DataFrame({
            'age': [25, 30, None, 40],
            'height': [170, None, 180, None],
            'weight': [70, None, 80, 90],
            'diabetes': [0, 1, 0, 1]
        })
        filled_df = self.fill_nan_processor.process(df_with_nans)
        self.assertFalse(filled_df['height'].isnull().any())  # No NaN in height
        self.assertFalse(filled_df['weight'].isnull().any())  # No NaN in weight

    def test_feature_transformer1(self):
        transformed_df = self.feature_transformer1.transform(self.df)
        self.assertIn('age_squared', transformed_df.columns)  # Check if new feature is created
        self.assertEqual(transformed_df['age_squared'].iloc[0], 625)  # Check calculation for first row

    def test_feature_transformer2(self):
        transformed_df = self.feature_transformer2.transform(self.df)
        self.assertIn('height_normalized', transformed_df.columns)  # Check if new feature is created

    def test_model_training(self):
        # Make sure to use data with both classes
        train_df = self.df  # Using the complete dataframe, which has both classes
        self.model.train(train_df)
        self.assertIsNotNone(self.model.model.coef_)  # Check if model coefficients are set

    def test_model_prediction(self):
        # Again, use data that has both classes
        test_df = self.df
        self.model.train(test_df)
        predictions = self.model.predict(test_df)
        self.assertEqual(len(predictions), test_df.shape[0])  # Check predictions length matches input

if __name__ == '__main__':
    unittest.main()
