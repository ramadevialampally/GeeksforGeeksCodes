
class Solution:
    def shortestPath(self, adj, src):
        # code here
       
        from collections import deque
        res=[-1]*(len(adj))
        visited=[False]*(len(adj))
        q=deque()
        q.append(src)
        res[src]=0
        visited[src]=True
        while q:
            a=q.popleft()
            for i in adj[a]:
                if not visited[i]:
                    res[i]=res[a]+1
                    visited[i]=True
                    q.append(i)
        return res
        
        
        
        



#{ 
 # Driver Code Starts
# Initial Template for Python 3
from collections import deque

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        V = int(input())
        E = int(input())
        adj = [[] for _ in range(V)]

        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)  # Since the graph is undirected

        src = int(input())

        ob = Solution()
        ans = ob.shortestPath(adj, src)

        print(" ".join(map(str, ans)))
        print("~")
        tc -= 1

# } Driver Code Ends