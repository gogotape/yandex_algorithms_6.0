from __future__ import annotations

import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, val: str, level: int = None, children: list[Node] = None):
        self.val = val
        self.children = children if children else []
        self.level = level if level else 0
        self.parent = None
        self.number_of_descendants = 0


def find_number_of_descendants(filename: str) -> None:

    child_and_parents = []

    with open(filename) as f:
        for line in f.readlines()[1:]:
            child_and_parents.append(line.split())

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
            dfs(node, 0)
            break

    for node_name, node in sorted_nodes.items():
        print(node_name, node.number_of_descendants)


def dfs(root: Node, children):
    if not root:
        return (None, 0)

    if not root.children:
        return (None, 0)

    cnt = 0

    for child in root.children:
        cnt += 1 + dfs(child, children)[1]
    root.number_of_descendants = cnt
    return root, cnt


if __name__ == "__main__":
    res = find_number_of_descendants("input.txt")
