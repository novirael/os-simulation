from copy import deepcopy
from random import choice
from hard_drive import (
    FirstComeFirstServedAlgorithm,
    ShortestSeekTimeFirstAlgorithm,
    ElevatorAlgorithm,
    CircularElevatorAlgorithm
)

MAX_SIMULATION_TIME = 1000
MAX_BUFFER_SIZE = 100


def prepare_initial_buffer():
    _buffer = []
    for data in range(MAX_BUFFER_SIZE):
        if choice([True, False*9]):
            _buffer.append(True)
        else:
            _buffer.append(False)
    return _buffer


def test():
    initial_buffer = prepare_initial_buffer()

    algorithms = [
        FirstComeFirstServedAlgorithm(deepcopy(initial_buffer)),
        # ShortestSeekTimeFirstAlgorithm(deepcopy(initial_buffer)),
        # ElevatorAlgorithm(deepcopy(initial_buffer)),
        # CircularElevatorAlgorithm(deepcopy(initial_buffer))
    ]

    for time_unit in range(MAX_SIMULATION_TIME):
        new_request = None
        if choice([True, False*99]):
            new_request = (0, True)
        for alg in algorithms:
            alg.motion(new_request=new_request)


if __name__ == "__main__":
    test()
