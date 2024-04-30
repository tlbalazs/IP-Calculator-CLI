def DecimalToBinary(octets):
    octets_bin = []
    for x in octets:
        x = int(x)
        octets_bin.append(f'{x:08b}')
    return octets_bin
