class Solution:
	def floodFill(self, image, sr, sc, newColor):
		#Code here
		def dfs(image,sr,sc,newcolor,source):
		    if sr<0 or sr>=len(image) or sc<0 or sc>=len(image[0]):
		        return
		    if image[sr][sc]!=source or image[sr][sc]==newcolor:
		        return
		    image[sr][sc]=newcolor
		    dfs(image,sr-1,sc,newcolor,source)
		    dfs(image,sr+1,sc,newcolor,source)
		    dfs(image,sr,sc-1,newcolor,source)
		    dfs(image,sr,sc+1,newcolor,source)
		source=image[sr][sc]
		dfs(image,sr,sc,newColor,source)
		return image
		    
		   



#{ 
 # Driver Code Starts
T = int(input())  # Read number of test cases
for i in range(T):
    n = int(input())
    m = int(input())

    # Reading the image matrix
    image = []
    for _ in range(n):
        image.append(list(map(int, input().split())))

    # Read starting row, column, and new color
    sr = int(input())
    sc = int(input())
    newColor = int(input())

    # Create an instance of the Solution class and apply floodFill
    obj = Solution()
    ans = obj.floodFill(image, sr, sc, newColor)

    # Print the modified image
    for row in ans:
        print(" ".join(map(str, row)))

    # Print the separator
    print("~")

# } Driver Code Ends