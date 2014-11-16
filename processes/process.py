from __future__ import print_function
import uuid

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


class ExecuteProcess(object):
    def __init__(self, queue=None):
        self.queue = None
        self.time_counter = 0
        self.summary_wait_time = 0
        self.summary_processes = 0

    def set_wait_time(self, proc):
        wait_time = 0
        for number, process in enumerate(self.queue, start=1):
            if process == proc:
                break
            if number != len(self.queue):
                wait_time += process.executing_time
        proc.wait_time = wait_time

    def set_wait_time_for_all(self):
        if not self.queue.is_empty():
            self.queue.first.wait_time = 0
            for process in self.queue:
                self.set_wait_time(process)

    @property
    def average_wait_time(self):
        return self.summary_wait_time / self.summary_processes

    def incoming_process(self, process):
        self.queue.enqueue(process)
        self.set_wait_time(process)

    def outgoing_process(self):
        self.queue.dequeue()
        self.set_wait_time_for_all()

    def print_state(self, time):
        print('time', time)
        for process in self.queue.get_queue('id', 'wait_time', 'executing_time'):
            for desc, value in process.iteritems():
                print('{}: {:2}  '.format(desc, value), end="")
            print()

    def step(self, process=None):
        self.set_wait_time_for_all()
        self.time_counter += 1

        if process is not None:
            self.incoming_process(process)
            self.summary_wait_time += process.wait_time
            self.summary_processes += 1

        if not self.queue.is_empty():
            if self.time_counter >= self.queue.first.executing_time:
                self.time_counter = 0
                self.outgoing_process()


class ExecuteFirstComeFirstServedProcess(ExecuteProcess):
    def __init__(self, queue=None):
        super(ExecuteFirstComeFirstServedProcess, self).__init__(queue)
        self.queue = FirstInFirstOutQueue(queue)
        self.title = 'First Come First Served Algorithm'


class ExecuteShortestJobFirstProcess(ExecuteProcess):
    def __init__(self, queue=None):
        super(ExecuteShortestJobFirstProcess, self).__init__(queue)
        self.queue = ShortestSeekFirstQueue('executing_time', queue, False)
        self.title = 'Shortest Job First Algorithm'


class ExecuteShortestRemainingTimeFirstProcess(ExecuteProcess):
    def __init__(self, queue=None):
        super(ExecuteShortestRemainingTimeFirstProcess, self).__init__(queue)
        self.queue = ShortestSeekFirstQueue('executing_time', queue)
        self.title = 'Shortest Remaining Time First Algorithm'

    def incoming_process(self, process):
        if not self.queue.is_empty():
            remaining_time = self.queue.first.executing_time - self.time_counter
            if process.executing_time < remaining_time:
                self.queue.first.executing_time = remaining_time
        super(ExecuteShortestRemainingTimeFirstProcess, self).\
            incoming_process(process)


class ExecuteRoundRobinProcess(ExecuteProcess):
    def __init__(self, quantum, queue=None):
        super(ExecuteRoundRobinProcess, self).__init__(queue)
        self.queue = FirstInFirstOutQueue(queue)
        self.title = 'Round Robin Algorithm'
        self.quantum = quantum

    def outgoing_process(self):
        remaining_time = self.queue.first.executing_time - self.quantum
        if remaining_time > 0:
            self.queue.first.executing_time = remaining_time
            first_process = self.queue.first
            self.queue.enqueue(first_process)
        super(ExecuteRoundRobinProcess, self).outgoing_process()

    def step(self, process=None):
        self.set_wait_time_for_all()
        self.time_counter += 1

        if process is not None:
            self.incoming_process(process)
            self.summary_wait_time += process.wait_time
            self.summary_processes += 1

        if self.time_counter == self.quantum:
            self.time_counter = 0
            if not self.queue.is_empty():
                self.outgoing_process()
