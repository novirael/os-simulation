import re


class LastRecentlyUsedAlgorithm(object):
    def __init__(self, query, num_frames):
        self.query = query
        self.frames = []
        self.num_frames = num_frames
        self.page_faults = 0
        self.fault = False

    @property
    def title(self):
        return re.sub(r'([^A-Z])([A-Z])', r'\1 \2', self.__class__.__name__)

    def execute(self):
        request = self.query.pop(0)
        if request not in self.frames:
            self.step(request)
        else:
            self.frames.remove(request)
            self.frames.append(request)

        if self.fault:
            self.fault = False
            return True
        return False

    def step(self, request):
        if len(self.frames) >= self.num_frames:
            self.remove_page()
            self.page_faults += 1
            self.fault = True
        self.frames.append(request)

    def remove_page(self):
        del self.frames[0]
