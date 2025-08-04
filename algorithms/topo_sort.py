"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented
by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i,
meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible
path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

https://leetcode.com/problems/find-eventual-safe-states/
"""

from collections import defaultdict, deque
from typing import List

def eventual_safe_nodes(graph: List[List[int]]) -> List[int]:
    reverse_graph = {k: [] for k in range(len(graph))}
    queue = []
    for k, v in enumerate(graph):
        if len(v) < 1:
            queue.append(k)
        for i in v:
            reverse_graph[i].append(k)

    _degrees = {k: len(v) for k, v in enumerate(graph)}

    terminals = []
    while queue:
        i = queue.pop(0)
        terminals.append(i)
        _from = reverse_graph[i]
        for f in _from:
            _degrees[f] -= 1

            if _degrees[f] < 1:
                queue.append(f)

    return sorted(terminals)


def main():
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    print(eventual_safe_nodes(graph))

if __name__ == "__main__":
    main()