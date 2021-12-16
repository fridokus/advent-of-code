#!/usr/bin/python3

import time

with open('16.in') as f:
    t = f.read().strip()
    size = len(t) * 4
    transmission = list(bin(int(t, 16))[2:].zfill(size))

def prod(i):
    p = 1
    for n in i: p *= n
    return p

def bin_to_dec(b): return int(''.join(b), 2)

class Packet():
    def __init__(self):
        self.version_sum = 0

    def parse(self, packet):
        version, packet = packet[:3], packet[3:]
        self.version_sum += bin_to_dec(version)
        type_id, packet = packet[:3], packet[3:]
        type_id = bin_to_dec(type_id)
        if type_id == 4:
            groups = []
            while True:
                group, packet = packet[:5], packet[5:]
                groups += group[1:]
                if group[0] == '0': break
            return bin_to_dec(groups), packet

        length_type_id = packet.pop(0)
        if length_type_id == '0':
            length, packet = packet[:15], packet[15:]
            length = bin_to_dec(length)
            subpacket, packet = packet[:length], packet[length:]
            subrets = []
            while subpacket:
                subret, subpacket = self.parse(subpacket)
                subrets.append(subret)
        else:
            number, packet = packet[:11], packet[11:]
            number = bin_to_dec(number)
            subrets = []
            for _ in range(number):
                subret, packet = self.parse(packet)
                subrets.append(subret)
        if   type_id == 0: ret = sum(subrets)
        elif type_id == 1: ret = prod(subrets)
        elif type_id == 2: ret = min(subrets)
        elif type_id == 3: ret = max(subrets)
        elif type_id == 5: ret = subrets[0] > subrets[1]
        elif type_id == 6: ret = subrets[0] < subrets[1]
        elif type_id == 7: ret = subrets[0] == subrets[1]
        return ret, packet

packet = Packet()
print(packet.parse(transmission))
print(packet.version_sum)
