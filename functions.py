import array
import re


def check_input(input):
    ip_regex = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    prefix_regex = r"\/(3[0-2]|[12]?[0-9])\b"
    ip_is_valid = re.match(ip_regex, input.split("/")[0])
    prefix_is_valid = re.match(prefix_regex, input[-3:])

    if not ip_is_valid:
        raise ValueError("Wrong or missing IP parameter. "
                         "You must follow the IP address dotted-decimal format, such as 192.168.123.234/24!")
    if not prefix_is_valid:
        raise ValueError("Wrong or missing IP parameter. "
                         "You must follow the IP address dotted-decimal format, such as 192.168.123.234/24!")
    return True


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
