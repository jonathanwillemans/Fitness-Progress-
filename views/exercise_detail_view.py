import tkinter as tk
from tkinter import ttk
import pandas as pd

class ExerciseDetailView:
    def __init__(self, controller, exercise_name):
        self.controller = controller
        self.exercise_name = exercise_name
        self.root = tk.Toplevel()
        self.root.title(f"Exercise Details - {exercise_name}")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(self.root)
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        self.title_label = tk.Label(self.scrollable_frame, text=self.exercise_name, font=("Helvetica", 18))
        self.title_label.pack(pady=10)

        self.back_button = tk.Button(self.scrollable_frame, text="Back", command=self.root.destroy, width=20)
        self.back_button.pack(pady=10)

    def load_data(self):
        exercise_data = self.controller.get_exercise_data()
        for date, sets in exercise_data.items():
            self.create_exercise_frame(date, sets)

    def create_exercise_frame(self, date, sets):
        frame = ttk.Frame(self.scrollable_frame, borderwidth=2, relief="groove")
        frame.pack(fill="x", padx=10, pady=5)

        date_label = tk.Label(frame, text=date.strftime('%Y-%m-%d'), font=("Helvetica", 16), anchor="w")
        date_label.pack(fill="x", padx=5, pady=5)

        for i, set_info in enumerate(sets, start=1):
            notes = set_info['Notes'] if pd.notna(set_info['Notes']) else ""
            workout_note = set_info['Workout Note'] if pd.notna(set_info['Workout Note']) else ""
            set_text = f"Set {i}: {set_info['Weight']:.2f}kg x {set_info['Reps']} - {notes} {workout_note}"
            set_label = tk.Label(frame, text=set_text.strip(), font=("Helvetica", 14), anchor="w")
            set_label.pack(fill="x", padx=5)

    def show(self):
        self.root.deiconify()
