class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p:TreeNode, q: TreeNode) -> bool:

        a = []
        b = []

        def re(p):
            if p != None:
                if p.val != None:
                    a.append(p.val)
                    re(p.left)
                    re(p.right)
            else:
                a.append("null")
        re(p)
        def ro(p):
            if p != None:
                if p.val != None:
                    b.append(p.val)
                    ro(p.left)
                    ro(p.right)
            else:
                b.append("null")
        ro(q)

        if len(a) == len(b):
            for i in range(len(a)):
                if a[i] != b[i]:
                    return False
        else:
            return False

        return True