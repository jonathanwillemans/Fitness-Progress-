import tkinter as tk
from controllers.exercises_controller import ExercisesController

class ExercisesView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = ExercisesController(controller)
        label = tk.Label(self, text="Exercises Screen")
        label.pack(pady=10, padx=10)
        self.create_widgets()

    def create_widgets(self):
        unique_exercises = self.controller.get_unique_exercises()
        for exercise in unique_exercises:
            button = tk.Button(self, text=exercise, command=lambda ex=exercise: self.show_exercise_data(ex))
            button.pack()

    def show_exercise_data(self, exercise_name):
        exercise_data = self.controller.get_exercise_data(exercise_name)
        # Handle showing exercise data
        # For now, just print the data
        print(exercise_data)
