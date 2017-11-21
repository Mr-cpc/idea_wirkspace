from basic.bupt_2017_11_09.bstm import TreeNode


def lonunivpat(root: TreeNode) -> int:
    stk = []
    ans = 0
    while len(stk) or root is not None:
        while root is not None:
            ans = max(midt(root.left,root.val), midt(root.right,root.val))
            root = root.left
        root = stk.pop().right
    return ans


def midt(root: TreeNode,val:int):
    if root is None:
        return 0
    elif root.val == val:
        return 1 + max(midt(root.left,val),midt(root.right,val))
    else:
        return 0
