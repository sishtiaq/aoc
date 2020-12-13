
from input import t0, t1

def parse(spec):
    depart_time,bus_times = spec
    bus_times = [ b for b in bus_times if b != -42 ]
    return depart_time, bus_times

def closest_depart_time(target_time, interval):
    i =1
    while (True):
        if (i*interval > target_time):
            # bus#, departure_time, departure_time - target_time)
            return (interval, i*interval, i*interval - target_time)
        i += 1


def part1(spec):
    target_time, buses = parse(spec)
    nearby_buses = []
    for bus in buses:
        depart_time = closest_depart_time(target_time, bus)
        nearby_buses.append(depart_time)
    
    return sorted(nearby_buses, key=lambda t: t[2])
