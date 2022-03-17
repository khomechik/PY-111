from typing import Hashable, Mapping, Union
import networkx as nx
from queue import PriorityQueue


def dijkstra_algo(g: nx.DiGraph, current_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param current_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """

    visited = []
    total_costs = {node: float('inf') for node in g.nodes}
    total_costs[current_node] = 0

    pq = PriorityQueue()
    pq.put((0, current_node))

    while not pq.empty():
        (dist, current_node) = pq.get()
        visited.append(current_node)
        neighbours = g[current_node]
        for neighbour in neighbours:
            edge = g[current_node][neighbour]
            weight = edge['weight']
            if neighbour not in visited:
                old_cost = total_costs[neighbour]
                new_cost = total_costs[current_node] + weight
                if new_cost < old_cost:
                    pq.put((new_cost, neighbour))
                    total_costs[neighbour] = new_cost

    return total_costs
