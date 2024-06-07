import pandas as pd

class DataLoader:
    def __init__(self, data_file):
        self.data_file = data_file
        self.data = pd.read_csv(data_file, sep=';')
        self.data['Date'] = pd.to_datetime(self.data['Date'])

    def load_data(self):
        return self.data

    def get_exercise_data(self, exercise_name):
        return self.data[self.data['Exercise Name'] == exercise_name]

    def get_workout_data_by_date(self, date):
        return self.data[self.data['Date'].dt.date == pd.to_datetime(date).date()]

    def get_workout_data_by_datetime(self, datetime):
        return self.data[self.data['Date'] == pd.to_datetime(datetime)]

    def get_unique_exercises(self):
        return self.data['Exercise Name'].unique()

    def get_exercise_frequency(self):
        return self.data['Exercise Name'].value_counts().index.tolist()

    def get_exercise_unique_days(self):
        unique_days = self.data.groupby('Exercise Name')['Date'].nunique()
        return unique_days.sort_values().index.tolist()

    def sort_exercises_alphabetically(self, reverse=False):
        return sorted(self.get_unique_exercises(), reverse=reverse)

    def sort_exercises_by_frequency(self, reverse=False):
        return sorted(self.get_exercise_frequency(), key=lambda x: self.data[self.data['Exercise Name'] == x].shape[0], reverse=reverse)

    def sort_exercises_by_unique_days(self, reverse=False):
        unique_days = self.data.groupby('Exercise Name')['Date'].nunique()
        return unique_days.sort_values(ascending=not reverse).index.tolist()

    def get_exercise_sessions(self, exercise_name):
        exercise_data = self.data[self.data['Exercise Name'] == exercise_name]
        exercise_dict = {}
        for date, group in exercise_data.groupby('Date'):
            sets = group[['Weight', 'Reps', 'Notes']].to_dict('records')
            exercise_dict[date] = sets
        return exercise_dict
