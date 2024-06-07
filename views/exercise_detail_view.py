import tkinter as tk
from tkinter import ttk

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
        self.load_data()

    def create_widgets(self):
        self.title_label = tk.Label(self.frame, text=self.exercise_name, font=("Helvetica", 18))
        self.title_label.pack(pady=10)

        self.tree = ttk.Treeview(self.frame)
        self.tree['columns'] = ('Weight', 'Reps', 'Notes')
        self.tree.heading('#0', text='Date')
        self.tree.heading('Weight', text='Weight')
        self.tree.heading('Reps', text='Reps')
        self.tree.heading('Notes', text='Notes')
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.placeholder_label = tk.Label(self.frame, text="Hier komt meer info", font=("Helvetica", 14))
        self.placeholder_label.pack(pady=10)

        self.back_button = tk.Button(self.frame, text="Back", command=self.root.destroy, width=20)
        self.back_button.pack(pady=10)

    def load_data(self):
        exercise_data = self.controller.get_exercise_data()
        for date, sets in exercise_data.items():
            for set_info in sets:
                self.tree.insert('', 'end', text=date, values=(set_info['Weight'], set_info['Reps'], set_info['Notes']))

    def show(self):
        self.root.deiconify()
