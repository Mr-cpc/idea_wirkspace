

class Node(object):
    def __init__(self,val:int):
        self.left,self.right = None,None
        self.val = val


def traverse(root:Node, res:list,nd:Node,cur:list):
    if root is None or len(res) == 1:
        return
    elif root is nd:
        res.append(cur[:])
    else:
        cur.append(root)
        traverse(root.left,res,nd,cur[:])
        traverse(root.right,res,nd,cur[:])


def find_path(nd:Node,root:Node) -> list:
    res = []
    traverse(root,res,nd,[])
    return res[0]


def find_paths(nds:set,root:Node) ->list:
    res = []
    traverse(root,res,nds,[])
    return res

def traverses(root:Node, res:list,nds:set,cur:list):
    if root is None or len(res) == len(nds):
        return
    elif root in nds:
        res.append(cur[:])
    else:
        cur.append(root)
        traverses(root.left,res,nds,cur[:])
        traverses(root.right,res,nds,cur[:])

'''
really silly,search the par the same time has no meaning only if the nd1 and nd2 are on the same level
'''
# def par(nd1:Node,nd2:Node,root:Node):
#     s = []
#     res = []
#     while len(s) or root is not None:
#         while root is not None:
#             s.append(root)
#             root = root.left
#
#         root = s.pop()
#         if nd1 in (root.left,root.right):
#             res.append(root)
#             print(nd1.val)
#             if len(res) == 2:
#                 return tuple(res)
#         if nd2 in (root.left,root.right):
#             res.append(root)
#             print(nd2.val)
#             if len(res) == 2:
#                 return tuple(res)
#         root = root.right




def lca(nd1:Node,nd2:Node,root:Node) ->Node:
    if nd2 in (nd1.left,nd1.right):
        return nd1.val
    elif nd1 in (nd2.left,nd2.right):
        return nd2.val
    elif nd1 is root:
        return nd1.val
    elif nd2 is root:
        return nd2.val
    else:
        path1 = find_path(nd1,root)
        path2 = find_path(nd2,root)
        path1,path2 = (path1,path2) if len(path1) <= len(path2) else (path2,path1)
        while len(path1):
            node = path1.pop()
            if node in path2:
                return node.val



rt = Node(1)
left = Node(2)
right = Node(3)
rt.left = left
rt.right = Node(3)

print(lca(rt.left,rt.right,rt))
















