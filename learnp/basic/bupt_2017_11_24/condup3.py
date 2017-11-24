def condup3(nums:list,k:int,t:int) -> bool:
    for idx,val in enumerate(nums):
        dis = 1
        while dis <= k and idx + k < len(nums):
            if abs(nums[k+idx] - val) <= t:
                return True
    return False



def condup_3(nums:list,k:int,t:int):
    bst = Bst(k,t)
    for idx,num in enumerate(nums):
        if bst.insert(TreeNode((num,idx))):
            return True
    else:
        return False

class Bst:
    def __init__(self,k,t):
        self.root = None
        self.k = k
        self.t = t

    def insert(self,node:TreeNode):
        flag = False
        if self.root is None:
            self.root = node
            return flag
        else:
            rt = self.root
            parent = None
            while rt is not None:
                if rt.val[0] == node.val[0]:
                    if node.val[1] - rt.val[1] <= self.k:
                        return True
                    else:
                        rt.val = node.val
                        return False
                elif rt.val[0] > node.val[0]:
                    if rt.val[0] - node.val[0] <= self.t and node.val[1] - rt.val[1] <= self.k:
                        return True
                    parent = rt
                    rt = rt.left
                else:
                    if node.val[0] - rt.val[0] <= self.t and node.val[1] - rt.val[1] <= self.k:
                        return True
                    parent = rt
                    rt = rt.right
        if node.val[0] < parent.val[0]:
            parent.left = node
        else:
            parent.right = node
        return False

    def search(self,val):
        rt = self.root
        parent = None
        while rt is not None:
            if rt.val == val:
                return parent,rt
            elif rt.val > val:
                parent = rt
                rt = rt.left
            else:
                parent = rt
                rt = rt.right
        return parent,rt
















class TreeNode(object):
    def __init__(self,val:tuple):
        self.val = val  #(num,idx)
        self.left = self.right = None














