#User function Template for python3
from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, adj : List[List[int]]) -> bool :
        # code 
        def acyclic(adj,i,visited,stack):
            if stack[i]:
                return True
            visited[i]=True
            stack[i]=True
            for j in adj[i]:
                if not visited[j] and acyclic(adj,j,visited,stack):
                    return True
                elif stack[j]:
                    return True
            stack[i]=False
            return False
        stack=[False]*(len(adj))
        visited=[False]*len(adj)
        for i in range(len(adj)):
            if not visited[i] and acyclic(adj,i,visited,stack):
                return True
        return False
            
            
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(adj):
            print(1)
        else:
            print(0)
        print("~")
# } Driver Code Ends