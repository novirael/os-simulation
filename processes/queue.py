

class FirstInFirstOutQueue(object):
    """
    Base interface for fifo queue based on python list
    """
    def __init__(self, queue=None):
        self._queue = queue if queue else []

    def __iter__(self):
        for el in self._queue:
            yield el

    def __len__(self):
        return len(self._queue)

    def enqueue(self, obj):
        self._queue.append(obj)

    def dequeue(self):
        if self._queue:
            return self._queue.pop(0)
        return None

    @property
    def first(self):
        try:
            return self._queue[0]
        except IndexError:
            return None

    def get_queue(self, *fields):
        if not fields:
            fields = ['id']
        return [
            {
                field: getattr(obj, field)
                for field in fields
            }
            for obj in self._queue
        ]

    def is_empty(self):
        return not bool(self._queue)


class ShortestSeekFirstQueue(object):
    """
    Base interface for ssf queue based on python list
    """
    def __init__(self, sort_by='id', queue=None):
        self.sort_by = sort_by
        if self._queue is not None:
            self._queue = queue
            self._sort_by_field(self.sort_by)

    def __iter__(self):
        for el in self._queue:
            yield el

    def enqueue(self, obj):
        self._queue.append(obj)
        self._sort_by_field(self.sort_by)

    def dequeue(self):
        if self._queue:
            return self._queue.pop(0)
        return None

    def get_queue(self, by_field='id'):
        return [
            getattr(obj, by_field) for obj in self._queue
        ]

    def _sort_by_field(self, field_name):
        self._queue.sort(key=lambda obj: getattr(obj, field_name))
