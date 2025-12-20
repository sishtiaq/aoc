# Day 8, Part 1.
import functools
import typing

def straight_line_distance(p1: typing.Tuple[int, int, int], p2: typing.Tuple[int, int, int]) -> float:
    """Calculates the Euclidean distance between two 3D points."""
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2) ** 0.5

def enumerate_pairwise_distances(points: set[typing.Tuple[int, int, int]]) -> typing.Dict[typing.Tuple[typing.Tuple[int, int, int], typing.Tuple[int, int, int]], float]:
    """Calculates pairwise distances between all points in the set."""
    distances = {}
    points_list = list(points)
    for i, p1 in enumerate(points_list):
        for _, p2 in enumerate(points_list[i + 1:]):
            distances[(p1, p2)] = straight_line_distance(p1, p2)
    return distances

def parse() -> set[typing.Tuple[int, int, int]]:
    """Parses input lines into a set of 3D junction coordinates."""
    junctions: set[typing.Tuple[int, int, int]] = set()
    while True:
        try:
            line = input()
            x, y, z = map(int, line.split(','))
            junctions.add((x, y, z))
        except EOFError:
            break
    return junctions

def find_circuit_containing_point(circuits: list[set[typing.Tuple[int, int, int]]], point: typing.Tuple[int, int, int]) -> typing.Optional[set[typing.Tuple[int, int, int]]]:
    """Finds and returns the circuit containing the given point, if any."""
    for circuit in circuits:
        if point in circuit:
            print(f"point {point} \in circuit {circuit}.")
            return circuit
    # should never get here
    return None

def main():
    junctions: set[typing.Tuple[int, int, int]] = parse()
    pairwise_distances = enumerate_pairwise_distances(junctions)
    pairwise_distances_sorted = sorted(pairwise_distances.items(), key=lambda item: item[1])
    take_len = 1000
    first_x_shortest_pairs = pairwise_distances_sorted[:take_len]
    points = set()
    for ((p1, p2), _d) in first_x_shortest_pairs:
        points.add(p1)
        points.add(p2)
    circuits = [set([p]) for p in points]
        
    # print(f"junctions: {junctions}")
    # print(f"distances: #{len(pairwise_distances_sorted)}")
    # for (p1, p2), dist in pairwise_distances_sorted:
    #     print(f"d({p1}, {p2}) =  {dist:.2f}")
    # print(f"circuits: {circuits}")

    for ((p1,p2),_d) in first_x_shortest_pairs:
        # print(f"Consider pair: ({p1}, {p2})")
        g1 = find_circuit_containing_point(circuits, p1)
        g2 = find_circuit_containing_point(circuits, p2)
        if g1 == g2:
            # print(f"{p1} and {p2} already in same circuit, skipping")
            pass
        else:
            # union-find
            # print(f"Connecting circuits of {p1} and {p2}")
            circuits.remove(g1)
            circuits.remove(g2)
            circuits.append(g1.union(g2))
        # print(f"Updated circuits: {sorted(circuits, key=lambda s: len(s))}")
    
    # Get the largest 3, multiply their lens. 
    u = sorted(circuits, key=lambda s: len(s))
    v = u[-3:]
    w = list(map(len, v))
    x = functools.reduce(lambda a,b: a * b, w, 1)
    print(f"mul {w} = {x}")

if __name__ == "__main__":
    main()