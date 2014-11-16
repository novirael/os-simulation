from copy import deepcopy
from random import randint, choice
from process import (
    Process,
    ExecuteFirstComeFirstServedProcess,
    ExecuteShortestJobFirstProcess,
    ExecuteShortestRemainingTimeFirstProcess,
    ExecuteRoundRobinProcess
)

MAX_SIMULATION_TIME = 500

MIN_EXECUTING_TIME = 5
MAX_EXECUTING_TIME = 10

QUANTUM = 8


def random_processes(
        quantity=1,
        timestamp=0,
        min_time=MIN_EXECUTING_TIME,
        max_time=MAX_EXECUTING_TIME
):
    if quantity == 1:
        return Process(randint(min_time, max_time), timestamp)
    return [
        Process(randint(min_time, max_time), timestamp)
        for process_id in range(quantity)
    ]


def test():
    random_init_processes = random_processes(7)

    algorithms = [
        ExecuteFirstComeFirstServedProcess(),
        ExecuteShortestJobFirstProcess(),
        ExecuteShortestRemainingTimeFirstProcess(),
        ExecuteRoundRobinProcess(quantum=QUANTUM)
    ]

    for process in deepcopy(random_init_processes):
        for alg in algorithms:
            alg.incoming_process(process)

    for time_unit in range(MAX_SIMULATION_TIME):
        new_process = None
        if choice([True, False, False, False]):
            new_process = random_processes(timestamp=time_unit)

        for alg in algorithms:
            alg.step(process=new_process)

    for alg in algorithms:
        print 'Wait time average for {title}: {wait_time}, {number} proc'.format(
            title=alg.title,
            wait_time=alg.average_wait_time,
            number=alg.summary_processes
        )


if __name__ == "__main__":
    test()
