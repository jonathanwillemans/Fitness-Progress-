from views.exercise_detail_view import ExerciseDetailView

class ExerciseDetailController:
    def __init__(self, exercise_name):
        self.exercise_name = exercise_name
        self.exercise_detail_view = ExerciseDetailView(self, exercise_name)

    def show_view(self):
        self.exercise_detail_view.show()
