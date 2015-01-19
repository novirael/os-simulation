import uuid

from random import choice


class Process(object):
    def __init__(self, load, id=None):
        self.id = id or str(uuid.uuid4())[:5]
        self.load = load


class Processor(object):
    executing_query = []
    qua_query = 0
    qua_migration = 0

    def __init__(self, id, threshold, threshold_min):
        self.id = id
        self.threshold = threshold
        self.threshold_min = threshold_min

    @property
    def load(self):
        return sum([
            process.load
            for process in self.executing_query
        ])

    @property
    def is_overload(self, count=True):
        if count:
            self.qua_query += 1
        return self.load > self.threshold

    @property
    def is_lowload(self):
        return self.load < self.load

    def add(self, process):
        self.executing_query.append(process)

    def take(self, processor):
        while processor.is_overload(count=False):
            self.qua_migration += 1
            process = processor.executing_query.pop()
            self.add(process)


class BaseProcessAllocationStrategy(object):
    def __init__(self, num, proc_threshold, proc_threshold_min, query, retry):
        self.processors = [
            Processor(i, proc_threshold, proc_threshold_min)
            for i in range(num)
        ]
        self.query = query
        self.retry = retry

    def get_random_processor(self, current_processor=None):
        if current_processor is None:
            return choice(self.processors)

        processors = [
            processor
            for processor in self.processors
            if processor is not current_processor
        ]
        return choice(processors)


class FirstProcessAllocationStrategy(BaseProcessAllocationStrategy):

    def execute(self):
        while self.query:
            process = self.query.pop()
            current_processor = self.get_random_processor()
            for _ in range(self.retry):
                processor = self.get_random_processor(current_processor)
                if not processor.is_overload:
                    processor.add(process)
                    break
            else:
                current_processor.add(process)


class SecondProcessAllocationStrategy(BaseProcessAllocationStrategy):

    def execute(self):
        while self.query:
            processor = self.get_random_processor()
            if processor.is_overload:
                self.add_process_to_free_random_processor()
            else:
                process = self.query.pop()
                processor.add(process)

    def add_process_to_free_random_processor(self):
        try:
            random_processor = choice([
                processor
                for processor in self.processors
                if not processor.is_overload
            ])
            process = self.query.pop()
            random_processor.add(process)
        except IndexError:
            print 'All processors are overload'


class ThirdProcessAllocationStrategy(BaseProcessAllocationStrategy):

    def execute(self):
        while self.query:
            processor = choice(self.processors)
            if processor.is_overload:
                self.add_process_to_free_random_processor()
            else:
                process = self.query.pop()
                processor.add(process)

            if processor.is_lowload:
                random_processor = self.get_random_processor(processor)
                if random_processor.is_overload:
                    processor.take(random_processor)

    def add_process_to_free_random_processor(self):
        try:
            random_processor = choice([
                processor
                for processor in self.processors
                if not processor.is_overload
            ])
            process = self.query.pop()
            random_processor.add(process)
        except IndexError:
            print 'All processors are overload'
