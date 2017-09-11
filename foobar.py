def prime(x):
    # check that number is greater that 1
    if x > 1:
        for i in range(2, x + 1):
            # check that only x and 1 can evenly divide x
            if x % i == 0 and i != x and i != 1:
                return False
        else:
            return True
    else:
        return False # if number is negative

def is_square(n):
    if n<1:
        return False
    else:
        for i in range(int(n/2)+1):
            if (i*i)==n:
                return True
        return False

min = 100
max = 100000

for i in range(min,max):
    if prime(i):
        print i, ": Foo"
    elif is_square(i):
        print i, ": Bar"
    else:
        print i, ": FooBar"
