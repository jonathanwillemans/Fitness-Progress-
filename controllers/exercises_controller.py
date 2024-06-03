from views.exercises_view import ExercisesView
from data.data_loader import DataLoader

class ExercisesController:
    def __init__(self):
        self.data_loader = DataLoader('data/strong.csv')
        self.exercises = self.get_exercises()
        self.sorted_exercises = self.data_loader.sort_exercises_alphabetically()
        self.exercises_view = ExercisesView(self)
        self.current_sort = 'alphabetical'
        self.sort_order = False  # False for ascending, True for descending

    def get_exercises(self):
        return self.data_loader.get_unique_exercises()

    def sort_exercises_by(self, criterion):
        if criterion != self.current_sort:
            self.sort_order = False if criterion == 'alphabetical' else True  # Set default sort order based on criterion
        else:
            self.sort_order = not self.sort_order  # Toggle sort order if same criterion

        self.current_sort = criterion

        if criterion == 'alphabetical':
            self.sorted_exercises = self.data_loader.sort_exercises_alphabetically(reverse=self.sort_order)
        elif criterion == 'frequency':
            self.sorted_exercises = self.data_loader.sort_exercises_by_frequency(reverse=self.sort_order)
        elif criterion == 'unique_days':
            self.sorted_exercises = self.data_loader.sort_exercises_by_unique_days(reverse=self.sort_order)
        
        self.exercises_view.load_exercises()

    def show_view(self):
        self.exercises_view.show()

    def show_exercise_detail(self, exercise_name):
        from controllers.exercise_detail_controller import ExerciseDetailController
        detail_controller = ExerciseDetailController(exercise_name)
        detail_controller.show_view()
