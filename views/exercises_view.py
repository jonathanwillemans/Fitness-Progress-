import tkinter as tk

class ExercisesView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Toplevel()
        self.root.title("Exercises")
        self.root.geometry("800x600")

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.create_widgets()
        self.load_exercises()

    def create_widgets(self):
        self.label = tk.Label(self.frame, text="List of Exercises", font=("Helvetica", 18))
        self.label.pack(pady=10)

        self.sort_frame = tk.Frame(self.frame)
        self.sort_frame.pack(pady=10)

        self.sort_alpha_button = tk.Button(self.sort_frame, text="Sort Alphabetically", command=self.sort_alphabetically, width=20)
        self.sort_alpha_button.pack(side=tk.LEFT, padx=5)

        self.sort_freq_button = tk.Button(self.sort_frame, text="Sort by Frequency", command=self.sort_by_frequency, width=20)
        self.sort_freq_button.pack(side=tk.LEFT, padx=5)

        self.sort_days_button = tk.Button(self.sort_frame, text="Sort by Unique Days", command=self.sort_by_unique_days, width=20)
        self.sort_days_button.pack(side=tk.LEFT, padx=5)

        self.listbox_frame = tk.Frame(self.frame)
        self.listbox_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.exercises_listbox = tk.Listbox(self.listbox_frame)
        self.exercises_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.exercises_listbox.bind("<<ListboxSelect>>", self.on_exercise_select)

        self.scrollbar = tk.Scrollbar(self.listbox_frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.exercises_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.exercises_listbox.yview)

        self.back_button = tk.Button(self.frame, text="Back", command=self.root.destroy, width=20)
        self.back_button.pack(pady=10)

    def load_exercises(self):
        self.exercises_listbox.delete(0, tk.END)
        exercises = self.controller.sorted_exercises
        for exercise in exercises:
            self.exercises_listbox.insert(tk.END, exercise)

    def sort_alphabetically(self):
        self.controller.sort_exercises_by('alphabetical')

    def sort_by_frequency(self):
        self.controller.sort_exercises_by('frequency')

    def sort_by_unique_days(self):
        self.controller.sort_exercises_by('unique_days')

    def on_exercise_select(self, event):
        selected_index = self.exercises_listbox.curselection()
        if selected_index:
            selected_exercise = self.exercises_listbox.get(selected_index)
            self.controller.show_exercise_detail(selected_exercise)

    def show(self):
        self.root.deiconify()
