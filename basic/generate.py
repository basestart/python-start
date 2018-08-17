import os

print list(range(1, 11))

print [d for d in os.listdir('.')]

d = {'x': 'A', 'y': 'B', 'z': 'C' }

for k, v in d.items():
    print k, '=', v

L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]

def fib(max):
    n, a, b = 0, 0, 1
    while(n < max):
        print b
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(5)