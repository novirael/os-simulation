import uuid

from random import choice
import re


class Process(object):
    def __init__(self, load, id=None):
        self.id = id or str(uuid.uuid4())[:5]
        self.load = load


class Processor(object):
    executing_query = []
    qua_query = 0
    qua_migration = 0
    sum_load = 0
    sum_qua = 0

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
    def load_average(self):
        return self.sum_load / self.sum_qua

    @property
    def is_overload(self, count=True):
        if count:
            self.qua_query += 1
        return self.load > self.threshold

    @property
    def is_lowload(self):
        return self.load < self.threshold_min

    def add(self, process):
        self.executing_query.append(process)
        self.sum_load += self.load
        self.sum_qua += 1

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

    @property
    def title(self):
        return re.sub(r'([^A-Z])([A-Z])', r'\1 \2', self.__class__.__name__)

    def get_random_processor(self, current_processor=None):
        if current_processor is None:
            return choice(self.processors)

        processors = [
            processor
            for processor in self.processors
            if processor is not current_processor
        ]
        return choice(processors)

    def outgoing_process(self):
        for processor in self.processors:
            if processor.executing_query and choice([True, False, False]):
                processor.executing_query.pop(0)

    def print_result(self):
        for processor in self.processors:
            print 'Processor %d' % processor.id
            print 'Queries: %d' % processor.qua_query
            print 'Migrations: %d' % processor.qua_migration
            print 'Load average: %d' % processor.load_average
        print '\n'

    def get_result(self):
        result = {
            'queries': 0,
            'migrations': 0,
            'load': 0
        }
        for processor in self.processors:
            result['queries'] += processor.qua_query
            result['migrations'] += processor.qua_migration
            result['load'] += processor.load_average

        return result


class FirstProcessAllocationStrategy(BaseProcessAllocationStrategy):

    def execute(self):
        while self.query:
            process = self.query.pop(0)
            current_processor = self.get_random_processor()
            for _ in range(self.retry):
                processor = self.get_random_processor(current_processor)
                if not processor.is_overload:
                    processor.add(process)
                    processor.qua_migration += 1
                    break
            else:
                current_processor.add(process)

            self.outgoing_process()


class SecondProcessAllocationStrategy(BaseProcessAllocationStrategy):

    def execute(self):
        while self.query:
            processor = self.get_random_processor()
            if processor.is_overload:
                self.add_process_to_free_random_processor()
                processor.qua_migration += 1
            else:
                process = self.query.pop(0)
                processor.add(process)

            self.outgoing_process()

    def add_process_to_free_random_processor(self):
        try:
            random_processor = choice([
                processor
                for processor in self.processors
                if not processor.is_overload
            ])
            process = self.query.pop(0)
            random_processor.add(process)
        except IndexError:
            pass
            # print 'All processors are overload'


class ThirdProcessAllocationStrategy(BaseProcessAllocationStrategy):

    def execute(self):
        while self.query:
            processor = choice(self.processors)
            if processor.is_overload:
                self.add_process_to_free_random_processor()
            else:
                process = self.query.pop(0)
                processor.add(process)

            if processor.is_lowload:
                random_processor = self.get_random_processor(processor)
                if random_processor.is_overload:
                    processor.take(random_processor)

            self.outgoing_process()

    def add_process_to_free_random_processor(self):
        try:
            random_processor = choice([
                processor
                for processor in self.processors
                if not processor.is_overload
            ])
            process = self.query.pop(0)
            random_processor.add(process)
        except IndexError:
            pass
            # print 'All processors are overload'
