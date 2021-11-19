import sys

n = int(sys.stdin.readline())
tree = {}
for i in range(n):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]


def preorder(root):
    if tree[root] != '.':
        print(root, end="")
    if tree[root][0] != '.':
        preorder(tree[root][0])
    if tree[root][1] != '.':
        preorder(tree[root][1])


def inorder(root):
    if tree[root][0] != '.':
        inorder(tree[root][0])
    if tree[root] != '.':
        print(root, end="")
    if tree[root][1] != '.':
        inorder(tree[root][1])


def postorder(root):
    if tree[root][0] != '.':
        postorder(tree[root][0])
    if tree[root][1] != '.':
        postorder(tree[root][1])
    if tree[root] != '.':
        print(root, end="")


preorder('A')
print()
inorder('A')
print()
postorder('A')
