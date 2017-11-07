class Node(object):

    def __init__(self,val:int):
        self.left,self.right = None,None
        self.val = val

















'''
such recursion can find all the paths only when the val of node are all positive 
'''
# def p(root:Node,k:int,cur:list,res:list):
#     if k == 0:
#         res.append(cur)
#     elif k < 0:
#         return
#     elif root is None:
#         return
#     else:
#         p(root.left,k,cur[:],res)
#         p(root.right,k,cur[:],res)
#         cur.append(root.val)
#         p(root.left,k-root.val,cur[:],res)
#         p(root.right,k-root.val,cur[:],res)

def pretra(root:Node,cur:list,res:list,k:int):
    if root is not None:
        if k == 0:
            cur.append()


def p(root:Node,k:int,cur:list,res:list):
    if root is None:
        return
    elif k == 0:
        res.append(cur[:])
        cur.append(root)
        p(root.left,-root.val,cur[:],res)
        p(root.right,-root.val,cur[:],res)
    else:
        p(root.left,k,cur[:],res)
        p(root.right,k,cur[:],res)
        cur.append(root.val)
        p(root.left,k-root.val,cur[:],res)
        p(root.right,k-root.val,cur[:],res)


def pasu(root:Node,k:int) ->int :
    res = []
    p(root,k,[],res)
    return len(res),res




rt = Node(10)
left = Node(5)
right = Node(-3)
rt.left = left
rt.right = right
ll = Node(3)
lr = Node(2)
rt.left.left = ll
rt.left.right = lr
rt.right.left = Node(11)
ll.left = Node(3)
ll.right = Node(2)
lr.right = Node(1)

print(pasu(rt,-3)[1])