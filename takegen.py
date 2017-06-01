"""Module for demo generator execution """


def take(count, iterable):
    """ Take items from the front of an iterable.
    :param count: The max num of items to retrieve
    :param iterable: the source data
    :return: At most 'Count' from 'iterable'
    """

    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)

if __name__ == '__main__':
    run_take()
