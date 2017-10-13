#no.2
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def condtruct(nums):
    res = ListNode(0)
    for num in nums:
        cur = ListNode(num)
        cur.next,res.next = res.next,cur
    return res.next

def reverse(nod):
    head = nod
    pre,cur = head,head.next
    while cur is not None:
        next = cur.next
        cur.next,pre,cur = pre,cur,next
    head.next = None
    return pre

def tostring(l):
    res = ""
    while l is not None:
        res += str(l.val) + "->"
        l = l.next
    return res[:len(res)-2]

def add(l1,l2):
    nod1,nod2 = l1,l2
    ans = ListNode(0)
    carry = 0
    while nod1 is not None and nod2 is not None:
        sum = (nod1.val + nod2.val + carry)
        val = sum % 10
        carry = sum // 10
        cur = ListNode(val)
        cur.next ,ans.next = ans.next,cur
        nod1 = nod1.next
        nod2 = nod2.next

    if nod1 is None and nod2 is None:
        if carry == 0:
            return reverse(ans.next)
        else:
            nod = ListNode(carry)
            nod.next = ans.next
            ans.next = nod
            return reverse(ans.next)
    else:
        nod = nod1 if nod1 is not None else nod2
        while nod is not None:
            sum = nod.val + carry
            val = sum % 10
            carry = sum // 10
            cur = ListNode(val)
            cur.next,ans.next = ans.next,cur
            nod = nod.next
        return reverse(ans.next)

l1 = condtruct([3,9,5])
l2 = condtruct([9,4,3])
print(tostring(add(l1,l2)))
