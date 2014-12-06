import re
from random import choice


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
        if len(self.frames) >= self.num_frames:
            self.remove_page()
            self.page_faults += 1
        self.frames.append(request)

    def remove_page(self):
        raise NotImplementedError


class FirstInFirstOutAlgorithm(BaseAlgorithm):
    def remove_page(self):
        del self.frames[0]


class TheOptimalAlgorithm(BaseAlgorithm):
    def remove_page(self):
        index = self.get_index()
        del self.frames[index]

    def get_index(self):
        # src_index = (frame_index, query_index)
        src_index = (0, 0)

        for i, el in enumerate(self.frames):
            try:
                query_index = self.query.index(el)
            except ValueError:
                return i

            if query_index > src_index[1]:
                src_index = (i, query_index)

        return src_index[0]


class LastRecentlyUsedAlgorithm(BaseAlgorithm):
    def execute(self):
        while self.query:
            request = self.query.pop(0)
            if request not in self.frames:
                self.step(request)
            else:
                self.frames.remove(request)
                self.frames.append(request)

    def remove_page(self):
        del self.frames[0]


class ApproximalLastRecentlyUsedAlgorithm(object):
    pass


class RandomAlgorithm(BaseAlgorithm):
    def remove_page(self):
        rand_page = choice(self.frames)
        self.frames.remove(rand_page)
