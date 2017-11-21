from queue import Queue

from idea_wirkspace.learnp.basic.bupt_2017_11_09.bstm import TreeNode


def trav(root: TreeNode, val) -> int:
    if root is None :
        return None
    q = Queue()
    q.put(root)
    while not q.empty():
        cur = q.get()
        if cur.left is not None:
            if cur.left != cur.right:
                return max(cur.left, cur.right)
            else:
                q.put(cur.left)
                q.put(cur.right)
    return None


def secmiv(root: TreeNode) -> int:
    if root is None or (None not in (root.left,root.right) and root.left.val == root.right.val):
        return -1
    else:
        if root.left != root.right:
            return max(root.left.val, root.right.val)
        else:
            l, r = trav(root.left, root.val), trav(root.right, root.val)
            return min(l, r) if l is not None and r is not None else -1 if l == r is None else l or r
a = TreeNode(2)
b = TreeNode(2)
c = TreeNode(2)
# a.left = b
# a.right = c
print(secmiv(a))
a = float("inf")
b = float("inf")
print(a == b)