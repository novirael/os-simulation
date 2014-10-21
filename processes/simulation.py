from copy import deepcopy
from random import randint
from process import (
    Process,
    ExecutingFirstComeFirstServedProcess,
    ExecutingShortestJobFirstProcess,
    ExecutingShortestRemainingTimeFirstProcess,
    ExecutingRoundRobinProcess
)


def random_queue(instance, quantity, min_time=0, max_time=1000):
    return [
        instance(randint(min_time, max_time), process_id)
        for process_id in range(quantity)
    ]


def test():
    random_process_queue = random_queue(Process, 500)
    fcfs = ExecutingFirstComeFirstServedProcess(
        deepcopy(random_process_queue)
    )
    sjf = ExecutingShortestJobFirstProcess(
        deepcopy(random_process_queue)
    )
    srtf = ExecutingShortestRemainingTimeFirstProcess(
        deepcopy(random_process_queue)
    )
    fcfs = ExecutingRoundRobinProcess(
        deepcopy(random_process_queue)
    )


if __name__ == "__main__":
    test()
