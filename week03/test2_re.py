import sys

T = int(sys.stdin.readline())


def dac(preorder, inorder):
    if len(preorder) == 1:
        return preorder
    elif len(preorder) == 0:
        return []
    elif len(inorder) == 1:
        return inorder
    elif len(inorder) == 0:
        return []
    root = preorder[0]
    root_idx = inorder.index(root)
    in_left = inorder[:root_idx]
    pre_left = preorder[1:len(in_left) + 1]
    in_right = inorder[root_idx + 1:]
    pre_right = preorder[len(in_left) + 1:]
    left = dac(pre_left, in_left)
    right = dac(pre_right, in_right)
    tree = left+right+[root]
    return tree


for _ in range(T):
    n = int(sys.stdin.readline())
    preorder = list(map(int, sys.stdin.readline().split()))
    inorder = list(map(int, sys.stdin.readline().split()))
    postorder = dac(preorder, inorder)
    print(*postorder)
