from copy import copy
from random import randint

from memory import (
    FirstInFirstOutAlgorithm,
    TheOptimalAlgorithm,
    LastRecentlyUsedAlgorithm,
    ApproximalLastRecentlyUsedAlgorithm,
    RandomAlgorithm
)

PAGE_SIZE = 100
FRAMES = 10

NUM_REQUESTS = 100


def test():
    query = [randint(1, PAGE_SIZE+1) for _ in range(NUM_REQUESTS)]
    algorithms = [
        FirstInFirstOutAlgorithm(copy(query), FRAMES),
        TheOptimalAlgorithm(copy(query), FRAMES),
        # LastRecentlyUsedAlgorithm(),
        # ApproximalLastRecentlyUsedAlgorithm(),
        RandomAlgorithm(copy(query), FRAMES)
    ]

    for alg in algorithms:
        alg.execute()
        print 'Page faults for {title}: {faults}/{requests}'.format(
            title=alg.title,
            faults=alg.page_faults,
            requests=NUM_REQUESTS
        )

if __name__ == "__main__":
    test()
