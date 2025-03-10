#User function Template for python3
from typing import List

class Solution:
    # Function to return Breadth First Traversal of given graph.
    
    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        # code here
        
        res=[]
        s=0
        v=len(adj)
        from collections import deque
        q=deque()
        q.append(s)
    
        visited=[False]*v
        visited[s]=True
        while q:
            curr=q.popleft()
            res.append(curr)
            for i in adj[curr]:
                if not visited[i] :
                    visited[i]=True
                    q.append(i)
        return res
            
            


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())  # Number of test cases
    for i in range(T):
        V = int(input())  # Number of vertices
        E = int(input())  # Number of edges
        adj = [[] for i in range(V)]  # Adjacency list
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)  # Undirected graph

        ob = Solution()
        ans = ob.bfsOfGraph(adj)
        print(" ".join(map(str, ans)))  # Print the BFS traversal result

# } Driver Code Ends