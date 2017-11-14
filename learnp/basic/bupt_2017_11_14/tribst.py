from basic.bupt_2017_11_09.bstm import TreeNode


def tribst(root:TreeNode,L:int,R:int) -> TreeNode:
    if root is None:
        return None
    else:
        if L <= root.val <= R:
            root.left = tribst(root.left,L,R)
            root.right = tribst(root.right,L,R)
            return root
        elif root.val < L:
            return tribst(root.right,L,R)
        else:
            return tribst(root.left,L,R)