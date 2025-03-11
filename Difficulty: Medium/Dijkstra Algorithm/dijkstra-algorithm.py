#{ 
 # Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys
import heapq
from typing import List, Tuple


# } Driver Code Ends

class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        # Your code here
        visited=[False]*(len(adj))
        import heapq
        q=[]
        m={}
        heapq.heappush(q,(0,src))
        m[src]=0
        while q:
            dist,a=heapq.heappop(q)
            if(visited[a]):
                continue
            visited[a]=True
            m[a]=dist
            for i in adj[a]:
                if not visited[i[0]]:
                    if i[0] not in m:
                        m[i[0]]=m[a]+i[1]
                    else:
                        if m[a] + i[1] < m[i[0]]:
                            m[i[0]] = m[a] + i[1]
                    heapq.heappush(q,(m[i[0]],i[0]))
        res=[0]*(len(adj))
        for i in range(len(adj)):
            res[i]=m[i]
        return res
                    
            
        


#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for _ in range(V)]
        for _ in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append((v, w))
            adj[v].append((u, w))
        src = int(input())
        ob = Solution()

        res = ob.dijkstra(adj, src)
        for i in res:
            print(i, end=" ")
        print()
        print("~")
# } Driver Code Ends