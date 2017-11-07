

class Node(object):
    def __init__(self,val:int):
        self.left,self.right = None,None
        self.val = val












def par(nd1:Node,nd2:Node,root:Node):
    s = []
    res = []
    while len(s) or root is not None:
        while root is not None:
            s.append(root)
            root = root.left

        root = s.pop()
        if nd1 in (root.left,root.right):
            res.append(root)
            print(nd1.val)
            if len(res) == 2:
                return tuple(res)
        if nd2 in (root.left,root.right):
            res.append(root)
            print(nd2.val)
            if len(res) == 2:
                return tuple(res)
        root = root.right




def lca(nd1:Node,nd2:Node,root:Node) ->Node:
    if nd2 in (nd1.left,nd1.right):
        return nd1
    elif nd1 in (nd2.left,nd2.right):
        return nd2
    else:
        pars = par(nd1,nd2,root)
        if pars[0] is pars[1]:
            return pars[0]
        else:
            return lca(pars[0],pars[1],root)



rt = Node(1)
left = Node(2)
right = Node(3)
rt.left = left
rt.right = Node(3)

print(lca(rt.left,rt.right,rt).val)
















