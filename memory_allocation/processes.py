from random import randint


proportional = {
    'proc1': {
        'first_page': 1,
        'last_page': 20,
        'frames': 5
    },
    'proc2': {
        'first_page': 21,
        'last_page': 30,
        'frames': 3
    },
    'proc3': {
        'first_page': 31,
        'last_page': 60,
        'frames': 8
    },
    'proc4': {
        'first_page': 61,
        'last_page': 100,
        'frames': 10
    },
    'proc5': {
        'first_page': 101,
        'last_page': 160,
        'frames': 15
    },
    'proc6': {
        'first_page': 161,
        'last_page': 180,
        'frames': 5
    },
    'proc7': {
        'first_page': 181,
        'last_page': 210,
        'frames': 3
    },
    'proc8': {
        'first_page': 211,
        'last_page': 270,
        'frames': 8
    },
    'proc9': {
        'first_page': 271,
        'last_page': 300,
        'frames': 10
    },
    'proc10': {
        'first_page': 301,
        'last_page': 360,
        'frames': 15
    },
}


def get_proportional_processes(number, times, min_frame_size, max_frame_size):
    proportional = {}
    for i in range(number):
        frame_size = randint(min_frame_size, max_frame_size)
        pages_size = frame_size * times
        proportional['proc{}'.format(i)] = {
            'first_page': i * pages_size + 1,
            'last_page': (i + 1) * pages_size,
            'frames': frame_size
        }
    return proportional


def get_equal_processes(number, pages_size, min_frame_size, max_frame_size):
    return {
        'proc{}'.format(i): {
            'first_page': i * pages_size + 1,
            'last_page': (i + 1) * pages_size,
            'frames': randint(min_frame_size, max_frame_size)
        } for i in range(number)
    }
