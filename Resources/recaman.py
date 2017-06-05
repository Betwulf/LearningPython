import sys
from itertools import count, islice

def sequence():
    """Generate Recaman's sequence."""
    seen = set()
    val = 0
    for nextval in count(1):
        if val <= nextval or val-nextval in seen:
            val += nextval
            seen.add(val)
            yield val
        else:
            val -= nextval
            seen.add(val)
            yield val

def write_sequence(filename, num):
    """ Write Recaman's sequence to a text file. """
    with open(filename, mode='wt', encoding='utf-8') as f:
        f.writelines("{0}\n".format(r) for r in islice(sequence(), num))

if __name__ == '__main__':
    s = sequence()
    for r in islice(s, 10):
        print(r)
    write_sequence("recaman.txt", 1000)
