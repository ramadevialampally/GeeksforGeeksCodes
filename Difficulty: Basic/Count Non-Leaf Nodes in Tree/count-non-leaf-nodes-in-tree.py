#User function Template for python3


# Structure of the node of the tree is as

'''class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None'''






# function should return the count of total number of non leaf nodes in the tree
class Solution:
    def countNonLeafNodes(self, root):
        # add code here
        if root is None:
            return 0
        c=0
        from collections import deque
        q=deque()
        q.append(root)
        while q:
            size=len(q)
            for i in range(size):
                x=q.popleft()
                if  x.left or x.right:
                    c+=1
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(100000)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    


if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        root=buildTree(input())
        ob = Solution()
        print(ob.countNonLeafNodes(root))
        
        

        print("~")
# } Driver Code Ends