from copy import deepcopy
from random import randint
from process import (
    FirstProcessAllocationStrategy,
    SecondProcessAllocationStrategy,
    ThirdProcessAllocationStrategy,
    Process
)


def test():
    params = {
        'num': 4,
        'proc_threshold': 80,
        'proc_threshold_min': 20,
        'query': [
            Process(randint(10, 60), i)
            for i in range(1000)
        ],
        'retry': 5,
    }
    simulations = [
        FirstProcessAllocationStrategy(**deepcopy(params)),
        SecondProcessAllocationStrategy(**deepcopy(params)),
        ThirdProcessAllocationStrategy(**deepcopy(params)),
    ]

    for simulation in simulations:
        simulation.execute()
        simulation.print_result()

if __name__ == "__main__":
    test()
