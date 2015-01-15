from random import randint

PAGE_SIZE = 100
FRAMES = 10

NUM_REQUESTS_PER_PROCESS = 1000


class MemoryAllocationSimulation():
    def __init__(self, processes):
        self.page_size = 100
        self.frames = 10
        self.number_processes = 10
        self.processes = processes
        self.set_query()

    def set_query(self):
        for details in self.processes.values():
            details['query'] = self.get_query(
                details['first_page'],
                details['last_page'],
                details['frames'],
                NUM_REQUESTS_PER_PROCESS
            )

    @staticmethod
    def get_query(first_page, last_page, frames_size, query_size):
        result = []

        # for _ in range(query_size):
        #     result.append(randint(first_page, last_page))

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
