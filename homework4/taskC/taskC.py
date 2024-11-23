from __future__ import annotations


import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, val: str, level: int = None, children: list[Node] = None):
        self.val = val
        self.children = children if children else []
        self.level = level if level else 0
        self.parent = None


def lca(u: Node, v: Node) -> Node:

    h1 = u.level
    h2 = v.level

    while h1 != h2:

        if h1 > h2:
            u = u.parent
            h1 -= 1
        else:
            v = v.parent
            h2 -= 1

    while u != v:
        u = u.parent
        v = v.parent

    return u


def find_lca(filename: str) -> None:

    child_and_parents = []

    with open(filename) as f:
        lines = f.readlines()
        n = int(lines[0])

        for i in range(1, n):
            line = lines[i]
            child_and_parents.append(line.split())

        requests = []
        for j in range(n, len(lines)):
            requests.append(lines[j].split())

    seen = {}

    for child, parent in child_and_parents:

        child_node = seen.get(child)
        parent_node = seen.get(parent)

        if not child_node:
            child_node = Node(child)

        if not parent_node:
            parent_node = Node(parent, children = [])

        child_node.parent = parent_node

        parent_node.children.append(child_node)

        seen[child] = child_node
        seen[parent] = parent_node

    sorted_nodes = dict(sorted(seen.items(), key=lambda x: x[0]))

    for node_name, node in sorted_nodes.items():
        if not node.parent:
            dfs(node)

    for request in requests:
        node1_name, node2_name = request
        node1 = seen[node1_name]
        node2 = seen[node2_name]
        res = lca(node1, node2)
        print(res.val)


def dfs(root: Node, depth=0):
    if not root:
        return

    root.level = depth

    for child in root.children:
        dfs(child, depth + 1)


if __name__ == "__main__":
    res = find_lca("input.txt")
