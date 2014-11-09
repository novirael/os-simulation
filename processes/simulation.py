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

    fcfs = ExecuteFirstComeFirstServedProcess()
    sjf = ExecuteShortestJobFirstProcess()
    srtf = ExecuteShortestRemainingTimeFirstProcess()
    rr = ExecuteRoundRobinProcess(quantum=QUANTUM)

    for process in deepcopy(random_init_processes):
        fcfs.incoming_process(process)
        sjf.incoming_process(process)
        srtf.incoming_process(process)
        rr.incoming_process(process)

    for time_unit in range(1000):
        new_process = None
        if choice([True, False, False, False]):
            new_process = random_processes(timestamp=time_unit)

        fcfs.step(process=new_process)
        sjf.step(process=new_process)
        srtf.step(process=new_process)
        rr.step(process=new_process)

    print 'Wait time averange for FirstComeFirstServed: {}, {} proc'.format(
        fcfs.average_wait_time, fcfs.summary_processes
    )
    print 'Wait time averange for ExecuteShortestJobFirstProcess: {}, {} proc'.format(
        sjf.average_wait_time, sjf.summary_processes
    )
    print 'Wait time averange for ExecuteShortestRemainingTimeFirstProcess: {}, {} proc'.format(
        srtf.average_wait_time, sjf.summary_processes
    )
    print 'Wait time averange for ExecuteRoundRobinProcess: {}, {} proc'.format(
        rr.average_wait_time, sjf.summary_processes
    )


if __name__ == "__main__":
    test()
