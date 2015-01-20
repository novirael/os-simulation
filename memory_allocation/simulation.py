from copy import deepcopy
from memory_allocation import MemoryAllocationSimulation
from processes import get_proportional_processes, get_equal_processes


def test():
    summary = {}
    equal = get_equal_processes(10, 30, 10, 10)
    proportional = get_proportional_processes(10, 3, 5, 15)
    simulations = {
        'Equals Simulation': MemoryAllocationSimulation(deepcopy(equal)),
        'Proportional Simulation': MemoryAllocationSimulation(proportional),
        'Page faults control Simulation': MemoryAllocationSimulation(
            deepcopy(equal),
            page_faults_control=True
        )
    }
    for name, simulation in simulations.iteritems():
        simulation.execute()

        print 'Page faults for {title}: {faults}/{requests}'.format(
            title=name,
            faults=simulation.page_faults,
            requests=simulation.num_requests
        )
        summary[name] = simulation.page_faults

    return summary


if __name__ == "__main__":
    test()
