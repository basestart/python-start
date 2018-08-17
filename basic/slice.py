from collections import Iterable

l = [1, 2, 3, 4, 5, 6]
p = []

for i in range(10):
    p.append(i)

print p
print p[0:3]
print p[:3]
print p[1:3]
print p[-2:]
print list(range(10))
print l[:5:2]
print l[::2]


d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print key

for val in d.values():
    print val

print isinstance('abc', Iterable)