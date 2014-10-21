

class FirstInFirstOutQueue(object):
    """
    Base interface for fifo queue based on python list
    """
    def __init__(self, queue=None):
        self.queue = queue if queue else []

    def enqueue(self, obj):
        self.queue.append(obj)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def get_queue(self, by_field='id'):
        return [
            getattr(obj, by_field) for obj in self.queue
        ]


class ShortestSeekFirstQueue(object):
    """
    Base interface for ssf queue based on python list
    """
    def __init__(self, sort_by='id', queue=None):
        self.sort_by = sort_by
        if queue is not None:
            self.queue = queue
            self._sort_by_field(self.sort_by)

    def enqueue(self, obj):
        self.queue.append(obj)
        self._sort_by_field(self.sort_by)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def get_queue(self, by_field='id'):
        return [
            getattr(obj, by_field) for obj in self.queue
        ]

    def _sort_by_field(self, field_name):
        self.queue.sort(key=lambda obj: getattr(obj, field_name))