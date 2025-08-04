"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional
edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that
already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi]
indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are
multiple answers, return the answer that occurs last in the input.

https://leetcode.com/problems/redundant-connection/
"""

from typing import List

def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    # initial state is each node is it's own parent
    parent = [i for i in range(len(edges) + 1)]

    def find(u: int) -> int:
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]

        return u

    def union(u: int, v: int) -> bool:
        u_root = find(u)
        v_root = find(v)

        if u_root == v_root:
            return False

        parent[v_root] = u_root
        return True

    for u, v in edges:
        if not union(u, v):
            return [u, v]

    return [-1, -1]

def main():
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    print(find_redundant_connection(edges))

if __name__ == "__main__":
    main()