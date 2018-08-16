# python function 返回的是tuple
def mabs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def nop () :
    pass

print mabs(-1)
print mabs('3')