from __future__ import annotations

import sys

from collections import defaultdict

sys.setrecursionlimit(100000)


def find_size_of_subtrees(filename: str):

    def dfs(node, parent):
        size = 1
        for neighbor in graph[node]:
            if neighbor != parent:
                size += dfs(neighbor, node)
        subtree_sizes[node] = size
        return size

    with open(filename) as f:
        data = f.readlines()
        V = int(data[0])

    graph = defaultdict(list)

    for i in range(1, V):
        u, v = map(int, data[i].split())
        graph[u].append(v)
        graph[v].append(u)
    subtree_sizes = [0] * (V + 1)
    dfs(1, -1)

    print(*subtree_sizes[1:])


if __name__ == "__main__":
    res = find_size_of_subtrees("input.txt")
