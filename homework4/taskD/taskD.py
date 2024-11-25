from __future__ import annotations

import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, val: int, level=0, left: Node = None, right: Node = None):
        self.val = val
        self.left = left
        self.right = right
        self.level = level


def do_bin_tree_operations(filename: str) -> None:

    with open(filename) as f:
        requests = f.readlines()

    root = None
    is_first_root = True
    for request in requests:

        if request.startswith("ADD"):
            val = int(request.split()[-1])
            to_add = Node(val=val)

            if is_first_root:
                is_first_root = False
                root = to_add
                root.level = 0
                print("DONE")
                continue

            res = add_node(root=root, to_add=to_add)
            print("ALREADY" if not res else "DONE")

        elif request.startswith("SEARCH"):
            target = int(request.split()[-1])
            res = find_node(root=root, target=target)
            print("YES" if res else "NO")

        elif request.startswith("PRINTTREE"):
            print_tree(root=root)
        else:
            raise ValueError(f"incorrect request!: {request}")


def find_node(root: Node, target: int):
    if not root:
        return
    if root.val == target:
        return True

    return find_node(root.left, target=target) or find_node(root.right, target=target)


def add_node(root: Node, to_add: Node, level=1):

    if to_add.val < root.val:
        if root.left is None:
            root.left = to_add
            to_add.level = level
            return to_add
        else:
            return add_node(root.left, to_add, level=root.left.level + 1)

    elif to_add.val > root.val:
        if root.right is None:
            root.right = to_add
            to_add.level = level
            return to_add
        else:
            return add_node(root.right, to_add, level=root.right.level + 1)
    else:
        return False


def print_tree(root: Node):
    if not root:
        return

    print_tree(root.left)
    print(root.level * ".", root.val, sep="")
    print_tree(root.right)


if __name__ == "__main__":
    do_bin_tree_operations("input.txt")
