#User function Template for python3
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:

    def areMirror(self, a, b):
        '''
        :param root1,root2: two root of the given trees.
        :return: True False
        
        '''
        #code here
        res1=[]
        from collections import deque
        q=deque()
        q.append(a)
        while q:
            x=q.popleft()
            res1.append(x.data)
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
        q1=deque()
        res2=[]
        q1.append(b)
        while q1:
            x=q1.popleft()
            res2.append(x.data)
            if x.right:
                q1.append(x.right)
            if x.left:
                q1.append(x.left)
        return res1==res2



#{ 
 # Driver Code Starts
#Contributed by Sudarshan Sharma
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
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        str1 = input()
        str2 = input()
        root1 = buildTree(str1)
        root2 = buildTree(str2)
        if Solution().areMirror(root1, root2) == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends