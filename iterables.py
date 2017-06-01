from pprint import pprint as pp
from math import factorial
from Isprime import is_prime
from Isprime import next_prime
from takegen import take
from distinctgen import distinct
from itertools import islice, count, chain
from lucasseries import lucas

''' itertools apparently has powerful thingies '''
import os
import glob

'''simple iterable, use split over a string to make a list'''
words = "Why sometimes I have believed as many as six impossible things before breakfast".lower().split()
lengths = [len(word) for word in words]
print(lengths)

factorial_num_size = [len(str(factorial(x))) for x in range(20)]
'''sets cannot have duplicates, so this could also be useful sometimes'''
factorial_set_num_size = {len(str(factorial(x))) for x in range(20)}
pp(factorial_num_size)
pp(factorial_set_num_size)

country_to_capital = {'UK': 'London',
                      'Brazil': 'Brazília',
                      'Morroco': 'Rabat',
                      'Sweden': 'Stockholm'}

'''for dictionaries, if you want access to both key and value, use the items method for some reason '''
countries = [c for c in country_to_capital]
print(countries)
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
print(country_to_capital)

'''this is of type dict_items'''
pp(country_to_capital.items())
pp(capital_to_country)

'''inserting into a dictionary will replace previous values, so watch out'''
override = {x[0]: x for x in words}
print(override)

file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
pp(file_sizes)


''' using an if clause to filter from the source '''
print(is_prime(243671))
primes = [x for x in range(101) if is_prime(x)]
print(primes)
prime_square_divisors = {x*x: (1, x, x*x) for x in range(20) if is_prime(x)}
pp(prime_square_divisors)


''' iterables! used under the hood by for and while loops '''
iterable = ['Spring', 'Summer', 'Fall', 'Winter']
iterator = iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
''' Calling again would throw an error StopIteration '''


'''Generators - lazy evaluation '''
def gen123():
    yield 1
    yield 2
    yield 3
    return

geninstance = gen123()

print(next(geninstance))
print(next(geninstance))
print(next(geninstance))
''' another call would generate the StopIteration exception '''
for v in gen123():
    print(v)

''' careful about the scope and instance of generators '''
primegen = next_prime(100, 201)
print("primegen: {}".format(next(primegen)))
print("primegen: {}".format(next(primegen)))
print("primegen: {}".format(next(primegen)))
print("primegen: {}".format(next(primegen)))
print("primegen: {}".format(next(primegen)))
print("primegen: {}".format(next(primegen)))
print("primegen: {}".format(next(primegen)))
print("primegen: {}".format(next(primegen)))
print("primegen: {}".format(next(primegen)))
print("primegen: {}".format(next(primegen)))
print("primegen: {}".format(next(primegen)))
print("primegen: {}".format(next(primegen)))


''' generators using generators in a lazy way '''
things = [1, 2, 1, 2, 4, 5, 6, 7, 7, 7, 9]
for item in take(3, distinct(things)):
    print(item)

''' sum of prime numbers under 20,000 '''
print(sum(x for x in range(20000) if is_prime(x)))

thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
list_thousand_primes = list(thousand_primes)
print("sum of the first thousand primes: {}".format(sum(list_thousand_primes)))


''' any and all built in is useful too '''
print("find truth: ", any([False, False, True]))
print("Any prime: ", any(is_prime(x) for x in range(1328, 1361)))


''' zip can combine lists interestingly '''
sunday = [5, 6, 7, 6, 7, 5]
monday = [21, 22, 23, 20, 21, 22]
tuesday = [100, 101, 102, 99, 100, 103, 103, 104]
for sun, mon in zip(sunday, monday):
    print("average = ", (sun + mon) / 2)

for temps in zip(sunday, monday, tuesday):
    print("min={:4.1f}, max={:4.1f}, avg={:4.1f}, ".format(min(temps), max(temps), sum(temps)/len(temps)))
pp(list(zip(sunday, monday, tuesday)))


''' chain can single list all days '''
print("temps are above zero: ", all(t > 0 for t in chain(sunday, monday, tuesday)))

for x in (islice((p for p in lucas() if is_prime(p)), 16)):
    print("lucas prime: ", x)
