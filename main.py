import functions

print("Add a IPv4 CIDR Block, i.e., a.b.c.d/n")
while True:
    try:
        cidr_block = input("Host Address and netmask: ")
        if functions.check_input(cidr_block):
            host_address = cidr_block.split("/")[0].split(".")
            prefix = int(cidr_block.split("/")[1])
            break
    except ValueError as e:
        print("An error occurred while checking the input parameter:", e)


ip_class = functions.check_ip_class(host_address)
is_private_network = functions.check_private_network(host_address, prefix)
netmask = functions.calculate_netmask(prefix)
wildcard = functions.calculate_wildcard_mask(netmask)
network_address = functions.calculate_network_address(host_address, netmask)
first_address = functions.calculate_first_address(network_address)
broadcast = functions.calculate_broadcast_address(network_address, wildcard)
last_address = functions.calculate_last_address(broadcast)
host_address_binary = functions.decimal_to_binary(host_address)
max_hosts = functions.calculate_max_hosts(prefix)

netmask_binary = functions.decimal_to_binary(netmask)
network_address_binary = functions.decimal_to_binary(network_address)
first_address_binary = functions.decimal_to_binary(first_address)
last_address_binary = functions.decimal_to_binary(last_address)
broadcast_binary = functions.decimal_to_binary(broadcast)
wildcard_binary = functions.decimal_to_binary(wildcard)

print("Host address:", '.'.join(host_address))
print("Netmask:", '.'.join(str(x) for x in netmask))
print("Wildcard:", '.'.join(str(x) for x in wildcard))
print("Network address:", '.'.join(str(x) for x in network_address), f"(Class {ip_class})")
print("First available address:", '.'.join(str(x) for x in first_address))
print("Last available address:", '.'.join(str(x) for x in last_address))
print("Broadcast address:", '.'.join(str(x) for x in broadcast))

print("\nBinary host address:", '.'.join(host_address_binary))
print("Binary netmask:", '.'.join(netmask_binary))
print("Wildcard binary:", '.'.join(wildcard_binary))
print("Binary network address:", '.'.join(network_address_binary))
print("First available address:", '.'.join(first_address_binary))
print("Last available address:", '.'.join(last_address_binary))
print("Broadcast address:", '.'.join(broadcast_binary))

print("\nMax available hosts in the network:", max_hosts,)
if is_private_network:
    print("(Private network)")

