from copy import deepcopy
from random import randint, choice
from process import (
    Process,
    ExecutingFirstComeFirstServedProcess,
    ExecutingShortestJobFirstProcess,
    ExecutingShortestRemainingTimeFirstProcess,
    ExecutingRoundRobinProcess
)


def random_processes(instance, quantity, min_time=0, max_time=1000):
    return [
        instance(randint(min_time, max_time), process_id)
        for process_id in range(quantity)
    ]


def test():
    random_init_processes = random_processes(Process, 1)
    random_incoming_processes = random_processes(Process, 5)

    fcfs = ExecutingFirstComeFirstServedProcess()
    # sjf = ExecutingShortestJobFirstProcess(
    #     deepcopy(random_init_processes)
    # )
    # srtf = ExecutingShortestRemainingTimeFirstProcess(
    #     deepcopy(random_init_processes)
    # )
    # rr = ExecutingRoundRobinProcess(
    #     deepcopy(random_init_processes)
    # )
    while True:
        fcfs.prints()
        fcfs.outgoing_process()
        if random_incoming_processes and choice([True, False]):
            fcfs.incoming_process(random_incoming_processes.pop())
        if not random_incoming_processes:
            if fcfs.is_waiting:
                break

    print 'Wait time averange for FirstComeFirstServed algorithm: {}'.format(
        fcfs.average_wait_time
    )


if __name__ == "__main__":
    test()
