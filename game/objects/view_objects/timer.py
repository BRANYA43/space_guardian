from time import time, time

from pygame.time import Clock

from game.objects.base_objects.widget import Widget
from game.utils.decorators import check_value_type


class Timer(Widget):
    def __init__(self):
        super().__init__('Timer', '0:00')
        self._clock: Clock | None = None
        self._milliseconds = 0

    # @check_value_type(Clock)
    def set_clock(self, value: Clock):
        self._clock = value

    def update(self):
        self._milliseconds += self._clock.get_time()
        seconds = self._milliseconds // 1000 % 60
        minutes = self._milliseconds // 1000 // 60
        self.set_value(f'{minutes}m {seconds}s')
