from ps0 import BinaryTree, BTvertex

def calculate_sizes(v: BTvertex) -> None:
    # Given vertex v and binary tree T, calculate size of all subtrees rooted at descendants of v. After running program on T.root, every vertex v in T should have v.size set to the size of the subtree rooted at v.
    while v.left or v.right:
        v.size += 1
        if v.parent:
            v.parent.size += 1
        if v.left:
            calculate_sizes(v.left, size)
        if v.right:
            calculate_sizes(v.right, size)

def main():
    root = BTvertex(120)
    tree = BinaryTree(root)
    tree.root.left = BTvertex(121)
    tree.root.right = BTvertex(124)
