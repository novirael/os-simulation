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

NUM_REQUESTS = 1000


def test(page_size, frames_size, num_requests, draw=False):
    summary = {}

    query = [randint(1, page_size+1) for _ in range(num_requests)]
    algorithms = [
        FirstInFirstOutAlgorithm(copy(query), frames_size),
        TheOptimalAlgorithm(copy(query), frames_size),
        LastRecentlyUsedAlgorithm(copy(query), frames_size),
        ApproximalLastRecentlyUsedAlgorithm(copy(query), frames_size),
        RandomAlgorithm(copy(query), frames_size)
    ]

    for alg in algorithms:
        alg.execute()
        if draw:
            print 'Page faults for {title}: {faults}/{requests}'.format(
                title=alg.title,
                faults=alg.page_faults,
                requests=num_requests
            )
        summary[alg.title] = alg.page_faults

    return summary


def statistic(frames, times=50):
    stat = {}

    for i in range(times):
        results = test(PAGE_SIZE, frames, NUM_REQUESTS)

        if not stat:
            stat = copy(results)
        else:
            for alg, result in results.iteritems():
                stat[alg] += result

    print stat

if __name__ == "__main__":
    # test(PAGE_SIZE, FRAMES, NUM_REQUESTS, draw=True)
    for frames in [10, 20, 30, 40]:
        statistic(frames)
