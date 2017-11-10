from basic.bupt_2017_11_09.bstm import TreeNode



def tra(rt:TreeNode) ->int:
    stk = []
    res = 0
    while rt is not None or len(stk):
        while rt is not None:
            stk.append(rt)
            rt = rt.left
        rt = stk.pop()
        res += rt.val
        rt = rt.right
    return res


def conbsgre(root:TreeNode) ->TreeNode:
    stk = []
    ans = root
    while root is not None or len(stk):
        while root is not None:
            root.val += tra(root.right)
            stk.append(root)
            root = root.left
        root = stk.pop().right
    return ans



















