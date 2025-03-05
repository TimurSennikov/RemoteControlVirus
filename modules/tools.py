import struct

def is_64_bit():
    return struct.calcsize('P') * 8 == 64