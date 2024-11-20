from __future__ import annotations


class Node:
    def __init__(self, val: str, level: int = None, children: list[Node] = None):
        self.val = val
        self.children = children if children else []
        self.level = level if level else 0
        self.parent = None


def find_levels_of_elements(filename: str) -> None:

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
            dfs(node)

    for node_name, node in sorted_nodes.items():
        print(node_name, node.level)


def dfs(root: Node, depth=0):
    global level
    if not root:
        return

    root.level = depth

    for child in root.children:
        dfs(child, depth + 1)


if __name__ == "__main__":
    res = find_levels_of_elements("input.txt")
