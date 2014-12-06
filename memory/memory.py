import re
from random import choice, randint


class BaseAlgorithm(object):
    def __init__(self, query, num_frames):
        self.query = query
        self.frames = []
        self.num_frames = num_frames
        self.page_faults = 0

    @property
    def title(self):
        return re.sub(r'([^A-Z])([A-Z])', r'\1 \2', self.__class__.__name__)

    def execute(self):
        while self.query:
            request = self.query.pop(0)
            if request not in self.frames:
                self.step(request)

    def step(self, request):
        if len(self.frames) <= self.num_frames:
            self.frames.append(request)
        else:
            self.remove_page()

    def remove_page(self):
        raise NotImplementedError


class FirstInFirstOutAlgorithm(object):
    pass


class TheOptimalAlgorithm(object):
    pass


class LastRecentlyUsedAlgorithm(object):
    pass


class ApproximalLastRecentlyUsedAlgorithm(object):
    pass


class RandomAlgorithm(BaseAlgorithm):
    def remove_page(self):
        rand_page = choice(self.frames)
        self.frames.remove(rand_page)
        self.page_faults += 1
