#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        # code here
        visited=[False]*len(adj)
        a=self.dfs(adj,visited,0,[])
        return a
    def dfs(self,adj,visited,s,k):
        visited[s]=True
        k.append(s)
        for i in adj[s]:
            if not visited[i]:
                self.dfs(adj,visited,i,k)
        return k
                
        
            


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    while T > 0:
        V, E = map(int, input().split())
        # Create adjacency list with V vertices
        adj = [[] for i in range(V)
               ]  # List of lists (vector of vectors equivalent)

        # Reading edges
        for i in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)

        # Create an object of Solution class
        ob = Solution()
        ans = ob.dfsOfGraph(adj)

        # Printing the result
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
        T -= 1
        print("~")
# } Driver Code Ends