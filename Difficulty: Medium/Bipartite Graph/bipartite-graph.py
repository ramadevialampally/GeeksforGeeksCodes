class Solution:
	def isBipartite(self, adj):
		#code here
	    def dfs(adj,color,colors,u):
	        color[u]=colors
	        for i in adj[u]:
	            if color[i]==-1:
	                dfs(adj,color,1-colors,i)
	            elif color[i]==colors:
	                return False
	        return True
	    color=[-1]*(len(adj))
	    for i in range(len(adj)):
	        if color[i]==-1:
    	        if not dfs(adj,color,0,i):
    	             return False
	    return True
	     
	        
#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V = int(input())
        E = int(input())
        adj = [[] for _ in range(V)
               ]  # Fixed unnecessary use of `i` in list comprehension
        for _ in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isBipartite(adj)
        if ans:  # Properly indented
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends