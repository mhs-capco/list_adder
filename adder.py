import itertools

def _add_stream(aa, bb):
    """adds two iterators, where each value in the interation represents a digit in a 
    decimal number.
    assumes:
      * the shorter stream has been zero-padded on the most-significant end
      * the least significant digits are first
    """
    carry = 0
    cc = []
    for aaa, bbb in zip(aa, bb):
       carry, val = _add_digit(aaa,bbb, carry)
       cc.append(val)
    if carry:
        cc.append(carry)
    return cc

def _add_digit(a, b, carry=0):
    """simple digit adder
    """
    c = a+b + carry
    return divmod(c, 10)

def add(a, b):
    """add two lists together
    """
    if len(a) < len(b):
        aa = itertools.chain(reversed(a), itertools.repeat(0))
        bb = reversed(b)
    elif len(b) < len(a):
        bb = itertools.chain(reversed(b), itertools.repeat(0))
        aa = reversed(a)
    else:
        aa = reversed(a)
        bb = reversed(b)
    cc = _add_stream(aa, bb)
    return list(reversed(cc))


