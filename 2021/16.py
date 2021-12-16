#!/usr/bin/python3

with open('16.in') as f:
    transmission = f.read().strip()
    transmission = list(bin(int(transmission, 16))[2:].zfill(len(transmission) * 4))

VERSION_SUM = 0

def increase_version_sum(version):
    global VERSION_SUM
    VERSION_SUM += version

def prod(i):
    p = 1
    for n in i: p *= n
    return p

def bin_to_dec(b): return int(''.join(b), 2)

def parse(packet):
    version, packet = bin_to_dec(packet[:3]), packet[3:]
    increase_version_sum(version)
    type_id, packet = bin_to_dec(packet[:3]), packet[3:]
    if type_id == 4:
        groups = []
        while True:
            group, packet = packet[:5], packet[5:]
            groups += group[1:]
            if group[0] == '0': break
        return bin_to_dec(groups), packet

    length_type_id = packet.pop(0)
    subrets = []
    if length_type_id == '0':
        length, packet = bin_to_dec(packet[:15]), packet[15:]
        subpacket, packet = packet[:length], packet[length:]
        while subpacket:
            subret, subpacket = parse(subpacket)
            subrets.append(subret)
    else:
        number, packet = bin_to_dec(packet[:11]), packet[11:]
        for _ in range(number):
            subret, packet = parse(packet)
            subrets.append(subret)
    if   type_id == 0: ret = sum(subrets)
    elif type_id == 1: ret = prod(subrets)
    elif type_id == 2: ret = min(subrets)
    elif type_id == 3: ret = max(subrets)
    elif type_id == 5: ret = subrets[0] > subrets[1]
    elif type_id == 6: ret = subrets[0] < subrets[1]
    elif type_id == 7: ret = subrets[0] == subrets[1]
    return ret, packet

print(parse(transmission))
print(VERSION_SUM)
