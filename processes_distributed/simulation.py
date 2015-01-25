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

    result = {}
    for simulation in simulations:
        simulation.execute()
        # simulation.print_result()
        result[simulation.title] = simulation.get_result()

    return result


def statistic(n):
    result = {}
    for i in range(n):
        current_result = test()

        if not result:
            result = deepcopy(current_result)
        else:
            for title, strategy_result in current_result.iteritems():
                result[title]['queries'] += strategy_result['queries']
                result[title]['migrations'] += strategy_result['migrations']
                result[title]['load'] += strategy_result['load']

    print result


if __name__ == "__main__":
    statistic(50)
