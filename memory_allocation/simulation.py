# from memory_allocation.memory import LastRecentlyUsedAlgorithm
from memory_allocation import MemoryAllocationSimulation
from processes import proportional, \
    get_equal_processes


def test():
    summary = {}
    proportional_simulation = MemoryAllocationSimulation(proportional)
    equalts_simulation = (#MemoryAllocationSimulation(
        get_equal_processes(10, 25, 15)
    )
    print equalts_simulation

    # lru = LastRecentlyUsedAlgorithm(query, frames_size)
    #
    # lru.execute()
    # print 'Page faults for {title}: {faults}/{requests}'.format(
    #     title=lru.title,
    #     faults=lru.page_faults,
    #     requests=num_requests
    # )
    # summary[lru.title] = lru.page_faults

    return summary


if __name__ == "__main__":
    test()
