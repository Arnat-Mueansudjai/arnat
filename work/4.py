
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
p=[1,3,3]
q=[1,1,3]
i=Solution()
print(i.isSameTree(p,q))        
        