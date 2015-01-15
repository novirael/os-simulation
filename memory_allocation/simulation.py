from memory_allocation.memory_allocation import MemoryAllocationSimulation
from processes import proportional, get_equal_processes


def test():
    summary = {}
    simulations = {
        'Proportional Simulation': MemoryAllocationSimulation(
            proportional
        ),
        'Equals Simulation': MemoryAllocationSimulation(
            get_equal_processes(10, 25, 15)
        )
    }
    for name, simulation in simulations.iteritems():
        simulation.execute()

        print 'Page faults for {title}: {faults}/{requests}'.format(
            title=name,
            faults=simulation.page_faults,
            requests=simulation.num_requests_per_process
        )
        summary[name] = simulation.page_faults

    return summary


if __name__ == "__main__":
    test()
