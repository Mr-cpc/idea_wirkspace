class TreeNode:
    def __init__(self,val):
        self.left ,self.right,self.val = None,None,val













def mod(rt:TreeNode)->int:
    serial = []
    stk = []
    while rt is not None or len(stk):
        while rt is not None:
            stk.append(rt)
            rt = rt.left
        rt = stk.pop()
        serial.append(rt.val)
        rt = rt.right
    ans = 0
    i = 1
    while i < len(serial):
        if serial[i] == serial[i-1]:
            cou = 1
            while serial[i] == serial[i-1]:
                cou += 1
                i += 1
            ans = max(ans,cou)
        else:
            i += 1

    return ans












