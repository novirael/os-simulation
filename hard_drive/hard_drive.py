
MAX_BUFFER_SIZE = 100


class BaseAccessAlgorithm(object):
    def __init__(self, initial_buffer):
        self.buffer = initial_buffer
        self.pointer = MAX_BUFFER_SIZE / 2
        self.motion_counter = 0
        self.counter = {
            'finished_request': 0,
            'motions': 0
        }

    @property
    def average_wait_time(self):
        return float(self.counter['motions']) / self.counter['finished_request']

    def motion(self, current):
        if current < self.pointer:
            self.pointer -= 1
            self.motion_counter += 1
        elif current > self.pointer:
            self.pointer += 1
            self.motion_counter += 1
        else:
            self.buffer.remove(current)
            self.counter['finished_request'] += 1
            self.counter['motions'] += self.motion_counter
            self.motion_counter = 0


class FirstComeFirstServedAlgorithm(BaseAccessAlgorithm):

    def step(self):
        if self.buffer:
            self.motion(self.buffer[0])


class ShortestSeekTimeFirstAlgorithm(BaseAccessAlgorithm):

    def _get_the_nearest(self):
        return min(self.buffer, key=lambda x: abs(x-self.pointer))

    def step(self):
        if self.buffer:
            self.motion(self._get_the_nearest())


class ElevatorAlgorithm(BaseAccessAlgorithm):
    def __init__(self, initial_buffer):
        super(ElevatorAlgorithm, self).__init__(initial_buffer)
        self.to_left = True

    def step(self):
        if self.buffer:
            self.motion()

    def motion(self):
        if self.pointer in self.buffer:
            self.buffer.remove(self.pointer)
            self.counter['finished_request'] += 1
            self.counter['motions'] += self.motion_counter
            self.motion_counter = 0

        if self.to_left:
            if self.pointer > 0:
                self.pointer -= 1
            else:
                self.to_left = False
        else:
            if self.pointer < MAX_BUFFER_SIZE - 1:
                self.pointer += 1
            else:
                self.to_left = True

        self.motion_counter += 1


class CircularElevatorAlgorithm(BaseAccessAlgorithm):

    def step(self):
        if self.buffer:
            self.motion()

    def motion(self):
        if self.pointer in self.buffer:
            self.buffer.remove(self.pointer)
            self.counter['finished_request'] += 1
            self.counter['motions'] += self.motion_counter
            self.motion_counter = 0

        if self.pointer > 0:
            self.pointer -= 1
            self.motion_counter += 1
        else:
            self.pointer = MAX_BUFFER_SIZE - 1
            self.motion_counter += 1
