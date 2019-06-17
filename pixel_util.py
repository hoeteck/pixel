from curve_ops import from_jacobian

from consts import q
from hash_to_field import hash_to_field

def print_g1(g1):
    print("g1 element:")
    g = from_jacobian(g1)
    print ("x coord", format(g[0], '100x'))
    print ("y coord", format(g[1], '100x'))

def print_g2(g2):
    print("g2 element:")
    g = from_jacobian(g2)
    print ("x coord", format(g[0][0], '100x'))
    print ("       ", format(g[0][1], '100x'))
    print ("y coord", format(g[1][0], '100x'))
    print ("       ", format(g[1][1], '100x'))

def hr(msg, ctr):
    if not isinstance(msg, bytes):
        raise ValueError("Hr can't hash anything but bytes")
    return hash_to_field(msg, ctr, q, 1)[0]
