from random import randint

from memory import LastRecentlyUsedAlgorithm

PAGE_SIZE = 100
FRAMES = 10

NUM_REQUESTS_PER_PROCESS = 1000


class MemoryAllocationSimulation():
    def __init__(self, processes):
        self.processes = processes
        self.num_requests_per_process = NUM_REQUESTS_PER_PROCESS
        self.num_requests = self.num_requests_per_process * len(processes)
        self.set_query()

    @property
    def page_faults(self):
        return sum([
            process['algorithm'].page_faults
            for process in self.processes.values()
        ])

    def set_query(self):
        for details in self.processes.values():
            details['query'] = self.get_query(
                details['first_page'],
                details['last_page'],
                details['frames'],
                self.num_requests_per_process * 2
            )

    @staticmethod
    def get_query(first_page, last_page, frames_size, query_size):
        result = []

        radius = frames_size / 2
        page_size = last_page - first_page

        for i in range(query_size / page_size):
            for current_page in range(first_page, last_page):
                page = randint(
                    current_page - radius,
                    current_page + radius
                )
                if last_page >= page >= first_page:
                    result.append(page)
        return result

    def execute(self):
        for name, details in self.processes.iteritems():
            details['algorithm'] = LastRecentlyUsedAlgorithm(
                details['query'],
                details['frames']
            )

        for __ in range(self.num_requests_per_process):
            for name, details in self.processes.iteritems():
                if len(details['algorithm'].query):
                    details['algorithm'].execute()
