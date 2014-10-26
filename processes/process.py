from __future__ import print_function
import uuid
from copy import copy

from queue import (
    FirstInFirstOutQueue,
    ShortestSeekFirstQueue,
)


class Process(object):
    def __init__(self, time, timestamp, id=None):
        self.id = id or str(uuid.uuid4())[:5]
        self.timestamp = timestamp
        self.executing_time = time
        self.wait_time = 0


class ExecuteFirstComeFirstServedProcess(object):
    def __init__(self, queue=None):
        self.queue = FirstInFirstOutQueue(queue)
        self.executed = []
        self.counter = 0

    def set_wait_time(self, proc):
        wait_time = 0
        for number, process in enumerate(self.queue, start=1):
            if process == proc:
                break
            if number != len(self.queue):
                wait_time += process.executing_time
        proc.wait_time = wait_time

    def set_wait_time_for_all(self):
        self.queue.first.wait_time = 0
        for process in self.queue:
            self.set_wait_time(process)

    @property
    def average_wait_time(self):
        summary_wait_time = 0
        for process in self.executed:
            summary_wait_time += process.wait_time
        return summary_wait_time / len(self.executed)

    def incoming_process(self, process):
        self.queue.enqueue(process)
        self.set_wait_time(process)

    def outgoing_process(self):
        if not self.queue.is_empty():
            self.queue.dequeue()

    def print_state(self, time):
        print('fcfs', time)
        for process in self.queue.get_queue('id', 'wait_time', 'executing_time'):
            for desc, value in process.iteritems():
                print('{}: {:2}  '.format(desc, value), end="")
            print()

    def step(self, process=None):
        self.counter += 1

        if process is not None:
            self.incoming_process(process)
            self.executed.append(copy(process))

        if self.counter == self.queue.first.executing_time:
            self.counter = 0
            self.outgoing_process()
            self.set_wait_time_for_all()


class ExecuteShortestJobFirstProcess(object):
    def __init__(self, queue=None):
        self.queue = ShortestSeekFirstQueue('executing_time', queue)


class ExecuteShortestRemainingTimeFirstProcess(object):
    def __init__(self, queue=None):
        self.queue = ShortestSeekFirstQueue('executing_time', queue)


class ExecuteRoundRobinProcess(object):
    def __init__(self, queue=None):
        self.queue = FirstInFirstOutQueue(queue)
