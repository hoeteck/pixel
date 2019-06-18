from hashlib import sha256
from consts import q
from hash_to_field import hash_to_field
from util import print_g1_hex, print_g2_hex

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
        print_g2_hex(tsk[0])
        for i in range (1,len(tsk)):
            print ("%d-th element" %i)
            print_g1_hex (tsk[i])
    else:
        print("empty")

def print_sig(sig):
    print_g2_hex(sig[0])
    print_g1_hex(sig[1])

## this function concatenates the serialized group elements
## with in a tsk, and returns the bytes string
## this function is not used in the code
def serial_ssk(ssk):
    t = b""
    for e in ssk:
        t = t+ serialize(e)
    return t

## an instantiation of the G_0 function
## output = hash_to_field("G0_hash"| input, 0, q, Sha256, 1)
def hash_1(seed):
    s = b"G0_hash" + seed
    if not isinstance(s, bytes):
        raise ValueError("hash_1 can't hash anything but bytes")
    return hash_to_field(s, 0, q, 1)[0]

## an instantiation of the G_1 function
## output = sha256("G1_hash"| input)
def hash_2(seed):
    s = b"G1_hash" + seed
    if not isinstance(s, bytes):
        raise ValueError("hash_2 can't hash anything but bytes")
    t = sha256(s).digest()
    return t
