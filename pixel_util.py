from curve_ops import from_jacobian
from hashlib import sha256
from consts import q
from hash_to_field import hash_to_field
from serdes import serialize
from util import print_g1_hex, print_g2_hex

def print_g1(g1):
    print_g1_hex(g1)

def print_g2(g2):
    print_g2_hex(g2)

def print_sk(sk):
    print ("===========================")
    print ("printing secret key")
    print ("time vector", sk[0])
    for j in range (len(sk[1])):
        print("%d-th subsecret key:"%j)
        print_tsk(sk[1][j])
    print ("end of printing secret key")
    print ("===========================")

def print_tsk(tsk):
    if tsk!=[]:
        print ("0-th element")
        print_g2(tsk[0])
        for i in range (1,len(tsk)):
            print ("%d-th element" %i)
            print_g1 (tsk[i])
    else:
        print("empty")

## this function concatenates the serialized group elements
## with in a tsk, and returns the bytes string
def serial_ssk(ssk):
    t = b""
    for e in ssk:
        t = t+ serialize(e)
    return t

## a wrapper to hash_to_field algorithm with build-in modulus, etc
def hr(msg, ctr):
    if not isinstance(msg, bytes):
        raise ValueError("Hr can't hash anything but bytes")
    return hash_to_field(msg, ctr, q, 1)[0]


def hash_1(seed):
    s = b"G0_hash" + seed
    return hash_to_field(s, 0, q, 1)[0]

def hash_2(seed):
    s = b"G1+hash" + seed
    t = sha256(s).digest()
    return t
