from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    path_nodes = []
    visited_nodes = {node: False for node in g.nodes}
    wait_nodes = []
    wait_nodes.append(start_node)
    visited_nodes[start_node] = True

    while wait_nodes:
        current_node = wait_nodes.pop()
        neighbours = g[current_node]

        for neighbour in neighbours:
            if not visited_nodes[neighbour]:
                wait_nodes.append(neighbour)
                visited_nodes[neighbour] = True
        path_nodes.append(current_node)
    return path_nodes
