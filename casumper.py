import sys,struct

PYTHONUNBUFFERED = "true"

PY3K = sys.version_info >= (3, 0)

def readUtf(bytes, offset):
    length = struct.unpack(">h", bytes[offset + 0: offset + 2])[0]
    name = bytes[offset + 2:offset + length+2]
    return name


if PY3K:
    print "PY3K"
    source = sys.stdin.buffer
else:
    # Python 2 on Windows opens sys.stdin in text mode, and
    # binary data that read from it becomes corrupted on \r\n
    if sys.platform == "win32":
        # set sys.stdin to binary mode
        import os, msvcrt
        msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
    source = sys.stdin

while True:
    # read length
    str_length = source.read(8);
    if str_length == "":
        break

    length = struct.unpack_from('>LL', str_length)[1]


    # print "Key length:", length
    if length < 10 or length > 1000000000:
        print 'Wrong length'

    data = source.read(length)
    # TODO check CRC
    crc = struct.unpack_from('>LL', source.read(8))[1]

    table = readUtf(data, 0)
    key = readUtf(data, len(table) + 2)
    print table, ':', key

source.close()


 
