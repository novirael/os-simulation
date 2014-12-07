import re
from random import choice


class BaseAlgorithm(object):
    def __init__(self, query, num_frames):
        self.query = query
        self.frames = []
        self.num_frames = num_frames
        self.page_faults = 0
        self.is_order = False

    @property
    def title(self):
        return re.sub(r'([^A-Z])([A-Z])', r'\1 \2', self.__class__.__name__)

    def execute(self):
        while self.query:
            request = self.query.pop(0)
            if request not in self.frames:
                self.step(request)
            elif self.is_order:
                self.frames.remove(request)
                self.frames.append(request)

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
    def __init__(self, query, num_frames):
        super(LastRecentlyUsedAlgorithm, self).__init__(query, num_frames)
        self.is_order = True

    def remove_page(self):
        del self.frames[0]


class ApproximalLastRecentlyUsedAlgorithm(BaseAlgorithm):
    def __init__(self, query, num_frames):
        super(ApproximalLastRecentlyUsedAlgorithm, self).__init__(query, num_frames)
        self.is_order = True

    def execute(self):
        while self.query:
            request = self.query.pop(0)
            if request not in [el for (el, _) in self.frames]:
                self.step(request)
            elif self.is_order:
                fr = [el for (el, _) in self.frames]
                item = self.frames[fr.index(request)]
                self.frames.remove(item)
                self.frames.append(item)

    def step(self, request):
        if len(self.frames) >= self.num_frames:
            self.remove_page()
            self.page_faults += 1
        self.frames.append((request, 1))

    def remove_page(self):
        i = 0
        while True:
            el, bit = self.frames[i]
            if bit == 1:
                self.frames[i] = (el, 0)
            else:
                self.frames.remove((el, bit))
                break
            i += 1
            if i >= len(self.frames):
                i = 0


class RandomAlgorithm(BaseAlgorithm):
    def remove_page(self):
        rand_page = choice(self.frames)
        self.frames.remove(rand_page)
