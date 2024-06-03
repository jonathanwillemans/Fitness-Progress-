import tkinter as tk

class ExerciseDetailView:
    def __init__(self, controller, exercise_name):
        self.controller = controller
        self.exercise_name = exercise_name
        self.root = tk.Toplevel()
        self.root.title(f"Exercise Details - {exercise_name}")
        self.root.geometry("800x600")

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.frame, text=self.exercise_name, font=("Helvetica", 18))
        self.title_label.pack(pady=10)

        self.placeholder_label = tk.Label(self.frame, text="Hier komt meer info", font=("Helvetica", 14))
        self.placeholder_label.pack(pady=10)

        self.back_button = tk.Button(self.frame, text="Back", command=self.root.destroy, width=20)
        self.back_button.pack(pady=10)

    def show(self):
        self.root.deiconify()
