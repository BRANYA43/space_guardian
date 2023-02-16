from game.objects import TextObject
from game.utils import decorators


class StatusBar:
    def __init__(self):
        self._score = 0
        self._live = 0
        self._score_view = TextObject(str(self._score))
        self._live_view = TextObject(str(self._live))

    @property
    def score(self) -> TextObject:
        return self._score_view

    @score.setter
    @decorators.is_type_value(int)
    def score(self, value: int):
        self._score = value
        self._score_view.set_text(str(self._score))

    @property
    def live(self) -> TextObject:
        return self._live_view

    @live.setter
    @decorators.is_type_value(int)
    def live(self, value: int):
        self._live = value
        self._live_view.set_text(str(self._live))
