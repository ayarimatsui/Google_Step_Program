# Google STEP Program week6
# homework1

def foo(b):
    # check the address of the input
    print('id(input b): %#08x' % id(b))
    print('id(first element of b): %#08x' % id(b[0]))
    # append a new element and check the address
    b.append(2)
    print('id(b): %#08x' % id(b))
    # also check the address of the last element appended
    print('id(first element of b): %#08x' % id(b[0]))
    print('id(last element of b): %#08x' % id(b[-1]))
    # connect another list and check the address
    b = b + [3]
    print('id(b): %#08x' % id(b))
    print('id(first element of b): %#08x' % id(b[0]))
    print('id(last element of b): %#08x' % id(b[-1]))
    # append a new element again and check the address
    b.append(4)
    print('id(b): %#08x' % id(b))
    print('id(first element of b): %#08x' % id(b[0]))
    print('id(last element of b): %#08x' % id(b[-1]))
    print('b:', b)


a = [1]
print('id(a): %#08x' % id(a))

foo(a)
print('a:', a)
print('id(a): %#08x' % id(a))