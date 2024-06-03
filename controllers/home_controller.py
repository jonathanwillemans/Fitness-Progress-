class HomeController:
    def __init__(self):
        from views.home_view import HomeView
        self.home_view = HomeView(self)

    def show_exercises(self):
        from controllers.exercises_controller import ExercisesController
        exercises_controller = ExercisesController()
        exercises_controller.show_view()

    def show_view(self):
        self.home_view.show()
