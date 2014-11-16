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
        if choice([False*10, True]):
            _buffer.append(position)
    return _buffer


def random_request(buff):
    if choice([False*10, True]):
        random_sector = randint(0, MAX_BUFFER_SIZE)
        if random_sector not in buff:
            return random_sector
    return None


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
            new_request = random_request(alg.buffer)
            alg.step(new_request)

    for alg in algorithms:
        print 'Wait time average for {title}:'.format(title=alg.title)
        print '{wait_time} average, {req} requests, {motions} motions'.format(
            wait_time=alg.average_wait_time,
            req=alg.counter['finished_request'],
            motions=alg.counter['motions'],
        )

if __name__ == "__main__":
    test()
