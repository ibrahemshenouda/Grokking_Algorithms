#!/usr/bin/python3
import Dijkstra


graph_1 = {}

graph_1["start"] = {}
graph_1["start"]["a"] = 6
graph_1["start"]["b"] = 2

graph_1["a"] = {}
graph_1["a"]["fin"] = 1

graph_1["b"] = {}
graph_1["b"]["a"] = 3
graph_1["b"]["fin"] = 5

graph_1["fin"] = {}


final_cost, optimal_path = Dijkstra.search(graph_1, "start", "fin")
print("Graph_1: Lowest Cost from start node to final node is: ", final_cost)
print("Graph_1: Optimal path to final node is : ", " -> ".join(optimal_path))


graph_2 = {}

graph_2["start"] = {}
graph_2["start"]["a"] = 5
graph_2["start"]["b"] = 2

graph_2["a"] = {}
graph_2["a"]["c"] = 4
graph_2["a"]["d"] = 2

graph_2["b"] = {}
graph_2["b"]["a"] = 8
graph_2["b"]["d"] = 7

graph_2["c"] = {}
graph_2["c"]["d"] = 6
graph_2["c"]["fin"] = 3

graph_2["d"] = {}
graph_2["d"]["fin"] = 1

graph_2["fin"] = {}


final_cost, optimal_path = Dijkstra.search(graph_2, "start", "fin")
print("Graph_2: Lowest Cost from start node to final node is: ", final_cost)
print("Graph_2: Optimal path to final node is : ", " -> ".join(optimal_path))

graph_3 = {}

graph_3["start"] = {}
graph_3["start"]["a"] = 10


graph_3["a"] = {}
graph_3["a"]["c"] = 20


graph_3["b"] = {}
graph_3["b"]["a"] = 1


graph_3["c"] = {}
graph_3["c"]["b"] = 1
graph_3["c"]["fin"] = 30


final_cost, optimal_path = Dijkstra.search(graph_3, "start", "fin")
print("Graph_3: Lowest Cost from start node to final node is: ", final_cost)
print("Graph_3: Optimal path to final node is : ", " -> ".join(optimal_path))

graph_4 = {}

graph_4["start"] = {}
graph_4["start"]["a"] = 2
graph_4["start"]["b"] = 2


graph_4["a"] = {}
graph_4["a"]["c"] = 2
graph_4["a"]["fin"] = 2


graph_4["b"] = {}
graph_4["b"]["a"] = 2


graph_4["c"] = {}
graph_4["c"]["b"] = -1
graph_4["c"]["fin"] = 2

final_cost, optimal_path = Dijkstra.search(graph_4, "start", "fin")
print("Graph_4: Lowest Cost from start node to final node is: ", final_cost)
print("Graph_4: Optimal path to final node is : ", " -> ".join(optimal_path))
