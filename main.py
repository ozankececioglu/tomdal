def tomdalling():
    with open(r"C:\ws\trash\personal\tomdal\q2.txt", 'r') as inp:
        bb = bytearray(base64.a85decode(inp.read()))

        # last = bb[-1] & 1
        for i in range(len(bb)):
            bb[i] = bb[i] ^ 0b01010101
            # olast = bb[i] & 1
            bb[i] = (bb[i] >> 1) | ((bb[i] & 1) << 7)
            # last = olast

        bb = str(bb, encoding='UTF8')
        print(bb)


def main():
    print(1 ^ 0b00000010)


if __name__ == '__main__':
    tomdalling()
    pass