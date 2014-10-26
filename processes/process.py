import uuid
from datetime import datetime

from queue import (
    FirstInFirstOutQueue,
    ShortestSeekFirstQueue,
)


class Process(object):
    def __init__(self, time, id=None):
        self.id = id or str(uuid.uuid4())[:5]
        self.timestamp = datetime.now()
        self.executing_time = time
        self.wait_time = 0


class ExecutingFirstComeFirstServedProcess(object):
    def __init__(self, queue=None):
        self.queue = FirstInFirstOutQueue(queue)
        self.counter = len(queue) if queue else 0
        self.summary_wait_time = 0

    def set_wait_time(self, process):
        wait_time = 0
        for process in self.queue:
            wait_time += process.executing_time
        process.wait_time = wait_time

    @property
    def average_wait_time(self):
        return self.summary_wait_time / self.counter

    def incoming_process(self, process):
        self.queue.enqueue(process)
        self.set_wait_time(process)

    def outgoing_process(self):
        if not self.queue.is_empty():
            self.counter += 1
            self.summary_wait_time += self.queue.first.wait_time
            self.queue.dequeue()

    @property
    def is_waiting(self):
        return self.queue.is_empty()

    def prints(self):
        print self.queue.get_queue('wait_time')


class ExecutingShortestJobFirstProcess(object):
    def __init__(self, queue=None):
        self.queue = ShortestSeekFirstQueue('executing_time', queue)


class ExecutingShortestRemainingTimeFirstProcess(object):
    def __init__(self, queue=None):
        self.queue = ShortestSeekFirstQueue('executing_time', queue)


class ExecutingRoundRobinProcess(object):
    def __init__(self, queue=None):
        self.queue = FirstInFirstOutQueue(queue)
