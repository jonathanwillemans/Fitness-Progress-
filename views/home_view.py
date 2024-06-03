import tkinter as tk

class HomeView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Fitness Tracker Home")
        self.root.geometry("800x600")

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.frame, text="Fitness Tracker", font=("Helvetica", 24))
        self.title_label.pack(pady=20)

        self.button_frame = tk.Frame(self.frame)
        self.button_frame.pack(pady=20)

        self.exercises_button = tk.Button(self.button_frame, text="Exercises", command=self.controller.show_exercises, width=20, height=2, font=("Helvetica", 14))
        self.exercises_button.pack(pady=10)

        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.root.quit, width=20, height=2, font=("Helvetica", 14))
        self.exit_button.pack(pady=10)

    def show(self):
        self.root.mainloop()
