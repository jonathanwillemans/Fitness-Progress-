import pandas as pd

class DataLoader:
    def __init__(self, data_file):
        self.data_file = data_file
        self.data = pd.read_csv(data_file, sep=';')
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.normalize_exercise_names()
        self.propagate_workout_notes()
        self.convert_weights_to_kg()

    def normalize_exercise_names(self):
        # Zorg ervoor dat alle oefennamen met een hoofdletter beginnen
        self.data['Exercise Name'] = self.data['Exercise Name'].str.title()

    def propagate_workout_notes(self):
        # Verplaats de workout note naar elke set
        for date, group in self.data.groupby('Date'):
            workout_note = group['Workout Note'].iloc[0] if 'Workout Note' in group.columns else ""
            if pd.notna(workout_note):
                self.data.loc[group.index, 'Workout Note'] = workout_note

    def convert_weights_to_kg(self):
        # Zet gewichten om naar kg als ze in lbs zijn aangeduid
        lbs_to_kg = 0.453592
        mask = self.data['Weight Unit'].str.lower() == 'lbs'
        self.data.loc[mask, 'Weight'] *= lbs_to_kg
        self.data.loc[mask, 'Weight Unit'] = 'kg'

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
        exercise_data = self.get_exercise_data(exercise_name)
        sessions = {}
        for date, group in exercise_data.groupby('Date'):
            sets = group[['Weight', 'Reps', 'Notes', 'Workout Note']].to_dict('records')
            sessions[date] = sets
        return sessions
