from copy import deepcopy
from random import randint, choice
from process import (
    Process,
    ExecuteFirstComeFirstServedProcess,
    ExecuteShortestJobFirstProcess,
    ExecuteShortestRemainingTimeFirstProcess,
    ExecuteRoundRobinProcess
)

MIN_EXECUTING_TIME = 5
MAX_EXECUTING_TIME = 10


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

    fcfs = ExecuteFirstComeFirstServedProcess()
    # sjf = ExecuteShortestJobFirstProcess()
    # srtf = ExecuteShortestRemainingTimeFirstProcess()
    # rr = ExecuteRoundRobinProcess()

    for process in deepcopy(random_init_processes):
        fcfs.incoming_process(process)

    for time_unit in range(1000):
        new_process = None
        if choice([True, False, False, False]):
            new_process = random_processes(timestamp=time_unit)

        fcfs.step(process=new_process)

    print 'Wait time averange for FirstComeFirstServed: {}, {} proc'.format(
        fcfs.average_wait_time, fcfs.summary_processes
    )


if __name__ == "__main__":
    test()
