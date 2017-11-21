from basic.bupt_2017_11_09.bstm import TreeNode
from queue import Queue


def trav(root: TreeNode, val) -> int:
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
    if root is None:
        return -1
    elif root.left == root.right is None:
        return -1
    else:
        if root.left != root.right:
            return max(root.left, root.right)
        else:
            l, r = trav(root.left, root.val), trav(root.right, root.val)
            return min(l, r) if l is not None and r is not None else -1 if l == r is None else l or r
