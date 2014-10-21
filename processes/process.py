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


class ExecutingFirstComeFirstServedProcess(object):
    def __init__(self, queue=None):
        self.queue = FirstInFirstOutQueue(queue)


class ExecutingShortestJobFirstProcess(object):
    def __init__(self, queue=None):
        self.queue = ShortestSeekFirstQueue('executing_time', queue)


class ExecutingShortestRemainingTimeFirstProcess(object):
    def __init__(self, queue=None):
        self.queue = ShortestSeekFirstQueue('executing_time', queue)


class ExecutingRoundRobinProcess(object):
    def __init__(self, queue=None):
        self.queue = FirstInFirstOutQueue(queue)
