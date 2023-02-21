from abc import ABC, abstractmethod


class CopyObject(ABC):
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def copy(self):
        pass

    @classmethod
    def create(cls, *args, **kwargs):
        return cls(*args, **kwargs)
