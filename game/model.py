class Model:
    def __init__(self):
        self._view = None

    def set_view(self, view):
        self._view = view

    def update(self):
        ...
