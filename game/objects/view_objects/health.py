from game.objects.base_objects.widget import Widget


class Health(Widget):
    def __init__(self):
        super().__init__('HP', '0')
