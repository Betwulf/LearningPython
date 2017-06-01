

def distinct(iterable):

    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinct():
    items = [2, 5, 5, 7, 6, 5]
    for item in distinct(items):
        print(item)


if __name__ == '__main__':
    run_distinct()

