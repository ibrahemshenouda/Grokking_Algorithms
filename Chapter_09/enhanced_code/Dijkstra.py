import math
infinity = math.inf

# finding the lowest cost in (costs) table not processed


def find_lowest_cost_node(costs, processed):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# search at (graph) from any selected node(start_node) to any selected node (end_node)
def search(graph, start_node, end_node):
    processed_nodes = set()
    parents = {}
    costs = {}

    # set every node cost (infinity) Until Dijkstra proves otherwise
    for node in graph:
        costs[node] = infinity

    costs[end_node] = infinity
    costs[start_node] = 0
    parents[start_node] = None

    # start node is the lowest node at first zero less than infinity
    current_node = find_lowest_cost_node(costs, processed_nodes)

    # find_lowest_cost_node return none if all nodes processed
    while current_node is not None:
        current_node_cost = costs[current_node]
        neighbors_of_current_node = graph.get(current_node, {})
        for neighbor_node in neighbors_of_current_node.keys():
            new_cost = current_node_cost + neighbors_of_current_node[neighbor_node]
            current_neighbor_cost = costs.get(neighbor_node, infinity)

            if current_neighbor_cost > new_cost:
                costs[neighbor_node] = new_cost
                parents[neighbor_node] = current_node

        processed_nodes.add(current_node)
        current_node = find_lowest_cost_node(costs, processed_nodes)

    # check if path to final node is exist
    if costs[end_node] == infinity:
        return infinity, []

    # find the optimal path
    path = []
    current = end_node
    while current != start_node:
        path.append(current)
        current = parents[current]
        if current == None:
            break

    path.append(start_node)
    path.reverse()

    # return the lowest cost(final node cost) and the optimal path
    return costs[end_node], path
