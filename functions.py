import array

def decimal_to_binary(octets):
    octets_bin = []
    for octet in octets:
        octet = int(octet)
        # octets_bin.append(f'{octet:08b}')
        octets_bin.append(bin(octet)[2:].zfill(8))
    return octets_bin


def calculate_netmask(prefix):
    mask = []
    for index in range(4):
        if index < prefix // 8:
            mask.append(255)
        else:
            mask.append(256 - pow(2,8 - (prefix % 8)))
            prefix = 0
    return mask


def calculate_hostid(host, netmask):
    hostid = [0, 0, 0, 0]
    for index in range(4):
        hostid[index] = (int(host[index]) & int(netmask[index]))
    return hostid


def calculate_first_address(host_id):
    first_address = [0, 0, 0, 0]
    for index in range(4):
        first_address[index] = host_id[index]
        if index == 3:
            first_address[index] = int(host_id[index]) + 1
    return first_address


def calculate_wildcard_mask(netmask):
    wildcard = [0, 0, 0, 0]
    for index in range(4):
        wildcard[index] = (1 << 8) - 1 - int(netmask[index])
    return wildcard


def calculate_broadcast_address(host, wildcard):
    broadcast = []
    for h, w in zip(host, wildcard):
        broadcast.append(h | w)
    return broadcast


def calculate_last_address(broadcast):
    last_address = broadcast.copy()
    last_address[3] = last_address[3] - 1
    return last_address
