import unittest
import numpy as np
import pandas as pd
from data.data_loader import DataLoader

class TestDataLoader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_loader = DataLoader('data/strong.csv')
        cls.data = cls.data_loader.load_data()

    def test_load_data(self):
        self.assertIsInstance(self.data, pd.DataFrame)
        self.assertGreater(len(self.data), 0)

    def test_get_exercise_data(self):
        exercise_data = self.data_loader.get_exercise_data('Bench Press (Barbell)')
        self.assertGreater(len(exercise_data), 0)
        self.assertTrue((exercise_data['Exercise Name'] == 'Bench Press (Barbell)').all())

    def test_get_workout_data_by_date(self):
        workout_data = self.data_loader.get_workout_data_by_date('2023-03-26')
        self.assertGreater(len(workout_data), 0)
        self.assertTrue((workout_data['Date'].dt.date == pd.to_datetime('2023-03-26').date()).all())

    def test_get_workout_data_by_datetime(self):
        workout_data = self.data_loader.get_workout_data_by_datetime('2023-03-26 17:52:29')
        self.assertGreater(len(workout_data), 0)
        self.assertTrue((workout_data['Date'] == pd.to_datetime('2023-03-26 17:52:29')).all())

    def test_get_unique_exercises(self):
        unique_exercises = self.data_loader.get_unique_exercises()
        self.assertIsInstance(unique_exercises, np.ndarray)
        self.assertGreater(len(unique_exercises), 0)

    def test_get_data_by_date_range(self):
        data_by_date_range = self.data_loader.get_data_by_date_range('2023-03-26', '2023-12-03')
        self.assertGreater(len(data_by_date_range), 0)
        self.assertTrue((data_by_date_range['Date'] >= pd.to_datetime('2023-03-26')).all())
        self.assertTrue((data_by_date_range['Date'] <= pd.to_datetime('2023-12-03')).all())

if __name__ == '__main__':
    unittest.main()
