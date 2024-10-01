class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=set()
        res=0

        def dfs(root):
            if(root + 1 not in visited):
                visited.add(root + 1)
                for neighbour in range(len(isConnected)):
                    if isConnected[root][neighbour] == 1 and neighbour + 1 not in visited:
                        dfs(neighbour)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i + 1 not in visited and isConnected[i][j] == 1:
                    dfs(i)
                    res+=1
        return res