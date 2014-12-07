from copy import copy
from random import randint

from memory import LastRecentlyUsedAlgorithm

PAGE_SIZE = 100
FRAMES = 10

NUM_REQUESTS = 1000


def test(page_size, frames_size, num_requests, draw=False):
    summary = {}

    query = [randint(1, page_size+1) for _ in range(num_requests)]
    lru = LastRecentlyUsedAlgorithm(copy(query), frames_size)
    allocations = []

    lru.execute()
    if draw:
        print 'Page faults for {title}: {faults}/{requests}'.format(
            title=lru.title,
            faults=lru.page_faults,
            requests=num_requests
        )
    summary[lru.title] = lru.page_faults

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
