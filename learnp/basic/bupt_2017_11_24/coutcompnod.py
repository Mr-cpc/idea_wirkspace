from basic.bupt_2017_11_09.bstm import TreeNode


def cotcompnod(root:TreeNode):
    if root is None:
        return 0
    else:
        return 1 + cotcompnod(root.left) + cotcompnod(root.right)

def other(root:TreeNode):
    if root is None:
        return 0
    elif root.left == root.right is None:
        return 1
    else:
        l_h, r_h = 0,0
        l_rt = r_rt = root
        while l_rt is not None:
            l_rt = l_rt.left
            l_h += 1
        while r_rt is not None:
            r_rt = r_rt.right
            r_h += 1
        if l_h == r_h:
            return (1 << (l_h)) - 1
        else:
            return other(root.left) + other(root.right) + 1
