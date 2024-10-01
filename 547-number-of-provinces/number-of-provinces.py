class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=set()
        res=0

        def dfs(root):
            if(root not in visited):
                visited.add(root)
                for neighbour in range(len(isConnected)):
                    if isConnected[root][neighbour] == 1 and neighbour not in visited:
                        dfs(neighbour)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i not in visited and isConnected[i][j] == 1:
                    dfs(i)
                    res+=1
        return res