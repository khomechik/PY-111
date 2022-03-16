from typing import Hashable, Mapping, Union
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, current_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param current_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    visited = {node: False for node in g.nodes}
    total_costs = {node: float("inf") for node in g.nodes}
    current_node = 1
    total_costs[current_node] = 0

    while True:
        visited[current_node] = True
        neighbours = g[current_node]
        for neighbour in neighbours:
            edge = g[current_node][neighbour]
            weight = edge['weight']
            total_costs[neighbour] = min(total_costs[neighbour], total_costs[current_node] + weight)

        not_visited_total_costs = {node: cost for node, cost in total_costs.items() if not visited[node]}
        if not not_visited_total_costs:
            break
        current_node, _ = min(not_visited_total_costs.items(), key=lambda item: item[0])
        return total_costs
