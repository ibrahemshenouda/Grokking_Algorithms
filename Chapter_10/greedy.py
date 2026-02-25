#!/usr/bin/python3
remaining_states = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

available_stations = {
    "kone": set(["id", "nv", "ut"]),
    "ktwo": set(["wa", "id", "mt"]),
    "kthree": set(["or", "nv", "ca"]),
    "kfour": set(["nv", "ut"]),
    "kfive": set(["ca", "az"])
}


final_stations = set()

while remaining_states:
    best_station_this_round = None
    best_coverage_this_round = set()

    for station_name, station_coverage in available_stations.items():
        useful_station = remaining_states & station_coverage
        if len(useful_station) > len(best_coverage_this_round):
            best_station_this_round = station_name
            best_coverage_this_round = useful_station

    remaining_states -= best_coverage_this_round
    final_stations.add(best_station_this_round)

print("Selected Stations:", final_stations)
