from views.exercise_detail_view import ExerciseDetailView
from data.data_loader import DataLoader

class ExerciseDetailController:
    def __init__(self, exercise_name):
        self.exercise_name = exercise_name
        self.data_loader = DataLoader('data/strong.csv')
        self.exercise_detail_view = ExerciseDetailView(self, exercise_name)

    def get_exercise_data(self):
        return self.data_loader.get_exercise_sessions(self.exercise_name)

    def show_view(self):
        self.exercise_detail_view.show()
