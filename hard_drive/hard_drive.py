
class FirstComeFirstServedAlgorithm(object):
    def __init__(self, initial_buffer):
        self.buffer = initial_buffer

    def motion(self, new_request=None):
        if new_request is not None:
            position, value = new_request
            self.buffer[position] = value


class ShortestSeekTimeFirstAlgorithm(object):
    pass


class ElevatorAlgorithm(object):
    pass


class CircularElevatorAlgorithm(object):
    pass
