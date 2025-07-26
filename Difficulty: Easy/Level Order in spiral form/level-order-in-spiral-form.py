'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''        

class Solution:
    def findSpiral(self, root):
        #code here
        from collections import deque
        q=deque()
        q.append(root)
        res=[]
        k=0
        left=False
        while q:
            a=[]
            for i in range(len(q)):
                v=q.popleft()
                a.append(v.data)
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
            if not left:
                a=a[::-1]
            left=not left
            res.extend(a)
        return res
                
                        
        