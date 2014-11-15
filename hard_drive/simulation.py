from copy import deepcopy
from random import choice, sample, randint
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
    for position in range(MAX_BUFFER_SIZE):
        if choice([False*10, True, False*0]):
            _buffer.append(position)
    return _buffer


def test():
    initial_buffer = sample(range(MAX_BUFFER_SIZE), 20)
    algorithms = [
        FirstComeFirstServedAlgorithm(deepcopy(initial_buffer)),
        ShortestSeekTimeFirstAlgorithm(deepcopy(initial_buffer)),
        ElevatorAlgorithm(deepcopy(initial_buffer)),
        CircularElevatorAlgorithm(deepcopy(initial_buffer))
    ]

    for time_unit in range(MAX_SIMULATION_TIME):
        for alg in algorithms:
            alg.step()

    for alg in algorithms:
        print 'Wait time average for {title}:'.format(title=alg.title)
        print '{wait_time} average, {req} requests, {motions} motions'.format(
            wait_time=alg.average_wait_time,
            req=alg.counter['finished_request'],
            motions=alg.counter['motions'],
        )

if __name__ == "__main__":
    test()
