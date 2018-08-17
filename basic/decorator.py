def log(f):
    def wrap(*argv, **kw):
        print "calling func", f.__name__
        return f(*argv, **kw)
    return wrap


@log
def now():
    print "2015-3-25"

now()



