import functions

input_address = input("Host Address and netmask: ")
host_address = input_address.split("/")[0].split(".")
prefix = int(input_address.split("/")[1])

netmask = functions.calculate_netmask(prefix)
wildcard = functions.calculate_wildcard_mask(netmask)
network_address = functions.calculate_hostid(host_address, netmask)
first_address = functions.calculate_first_address(network_address)
broadcast = functions.calculate_broadcast_address(network_address, wildcard)
last_address = functions.calculate_last_address(broadcast)
host_address_binary = functions.decimal_to_binary(host_address)

netmask_binary = functions.decimal_to_binary(netmask)
network_address_binary = functions.decimal_to_binary(network_address)
first_address_binary = functions.decimal_to_binary(first_address)
last_address_binary = functions.decimal_to_binary(last_address)
broadcast_binary = functions.decimal_to_binary(broadcast)
wildcard_binary = functions.decimal_to_binary(wildcard)

print("Host address:", '.'.join(host_address))
print("Netmask:", '.'.join(str(x) for x in netmask))
print("Wildcard:", '.'.join(str(x) for x in wildcard))
print("Network address:", '.'.join(str(x) for x in network_address))
print("First available address:", '.'.join(str(x) for x in first_address))
print("Last available address:", '.'.join(str(x) for x in last_address))
print("Broadcast address:", '.'.join(str(x) for x in broadcast))

print("Binary host address:", '.'.join(host_address_binary))
print("Binary netmask:", '.'.join(netmask_binary))
print("Wildcard binary:", '.'.join(wildcard_binary))
print("Binary network address:", '.'.join(network_address_binary))
print("First available address:", '.'.join(first_address_binary))
print("Last available address:", '.'.join(last_address_binary))
print("Broadcast address:", '.'.join(broadcast_binary))

