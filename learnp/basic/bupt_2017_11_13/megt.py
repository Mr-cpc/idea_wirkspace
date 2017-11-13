from basic.bupt_2017_11_09.bstm import TreeNode







def megt(t1:TreeNode,t2:TreeNode) ->TreeNode:
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    ans = TreeNode(t1.val+t2.val)
    ans.left = megt(t1.left,t2.left)
    ans.right = megt(t2.right,t1.right)
    return ans