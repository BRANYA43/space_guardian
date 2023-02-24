from game.objects.base_objects.widget import Widget

from game.utils.decorators import check_value_type


class Score(Widget):
    def __init__(self):
        self.default_value = '000000'
        self.score = 0
        super().__init__('Score', self.default_value)

    @check_value_type(int)
    def set_value(self, value: int):
        self.score += value
        text_score = str(self.score)
        count = len(self.default_value) - len(text_score)

        if count > 0:
            text_score = self.default_value[:count] + text_score
        super().set_value(text_score)
