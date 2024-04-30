import functions

host_address = input("Host Address: ")
ha_octets = host_address.split("/")[0].split(".")
prefix = int(host_address.split("/")[1])

ha_octets_bin = functions.DecimalToBinary(ha_octets)
print("Host address:", '.'.join(ha_octets))
print("Host address bin:", '.'.join(ha_octets_bin))

# mask = ["255" if i < prefix // 8 else "0" for i in range(4)]
# mask[3] = str(256 - 2**(prefix % 8))
# netmask = ".".join(mask)

# mask = []
# for index in range(4):
#     if index < prefix // 8:
#         mask.append(255)
#     else:
#         mask.append(256 - pow(2,8 - (prefix % 8)))
#         prefix = 0

# mask = [0, 0, 0, 0]
# for i in range(prefix):
#     mask[i // 8] += 1 << (7 - i % 8)

mask = []
for index in range(4):
    mask.append(256 - pow(2,8 - (prefix % 8)))

print(mask)