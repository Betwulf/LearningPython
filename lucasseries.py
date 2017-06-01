from takegen import take

def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b

for x in take(10, lucas()):
    print(x)
