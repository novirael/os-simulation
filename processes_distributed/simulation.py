from process import (
    FirstProcessAllocationStrategy,
    SecondProcessAllocationStrategy,
    ThirdProcessAllocationStrategy,
)


def get_query():
    return []


def test():
    params = {
        'num': 10,
        'proc_threshold': 80,
        'proc_threshold_min': 20,
        'query': get_query(),
        'retry': 5,
    }
    simulations = [
        FirstProcessAllocationStrategy(**params),
        SecondProcessAllocationStrategy(**params),
        ThirdProcessAllocationStrategy(**params),
    ]

    for simulation in simulations:
        simulation.execute()


if __name__ == "__main__":
    test()
