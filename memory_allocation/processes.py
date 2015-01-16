from random import randint


def get_proportional_processes(number, times, min_frame_size, max_frame_size):
    result = {}
    for i in range(number):
        frame_size = randint(min_frame_size, max_frame_size)
        pages_size = frame_size * times
        result['proc{}'.format(i)] = {
            'first_page': i * pages_size + 1,
            'last_page': (i + 1) * pages_size,
            'frames': frame_size
        }
    print 'Page size for proportional: %d' % result['proc{}'.format(number - 1)]['last_page']
    return result


def get_equal_processes(number, pages_size, min_frame_size, max_frame_size):
    result = {
        'proc{}'.format(i): {
            'first_page': i * pages_size + 1,
            'last_page': (i + 1) * pages_size,
            'frames': randint(min_frame_size, max_frame_size)
        } for i in range(number)
    }
    print 'Page size for equals: %d' % result['proc{}'.format(number - 1)]['last_page']
    return result
