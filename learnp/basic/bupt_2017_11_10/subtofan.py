from basic.bupt_2017_11_09.bstm import TreeNode


def trav(s,t):
    if None in (s, t):
        return s == t
    elif s.val == t.val:
        return trav(s.left, t.left) and trav(s.right, t.right)
    else:
        return False


def subofan(s:TreeNode, t:TreeNode)->bool:
    if s is None:
        return t is None
    if t is None:
        return s is None
    stk = []
    root = s
    while root is not None or len(stk):
        while root is not None:
            if root.val == t.val:
                f = trav(root.left,t.left) and trav(root.right,t.right)
                if f:
                    return f
            else:
                stk.append(root)
                root = root.left
        root = stk.pop().right
    return False
