from basic.bupt_2017_11_09.bstm import TreeNode


def sum_(root):
    if root is None:
        return 0
    else:
        return root.val + sum_(root.left)+ sum_(root.right)


def btt(root:TreeNode) ->int:
    stk = []
    pre = None
    ans = 0
    d = {}
    while root is not None or len(stk):
        while root is not None:
            stk.append(root)
            root = root.left

        root = stk[-1]
        if root.right in (None,pre):
            stk.pop()
            sum_rt = root.val
            if root.left in d:
                sum_rt += d[root.left]
            else:
                sum_rt += sum_(root.left)
            if root.right in d:
                sum_rt += d[root.right]
            else:
                sum_rt += sum_(root.right)
            d[root] = sum_rt
            ans += abs(d.get(root.left,0) - d.get(root.right,0))
            pre = root
            root = None
        else:
            root = root.right
    return ans