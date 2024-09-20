class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol=[]
        ans=[]
        n=len(nums)
        def help(nums):
            if(len(sol)==n):
                ans.append(sol[:])

            for i in nums:
                if i not in sol:
                    sol.append(i)
                    help(nums)
                    sol.pop()
        help(nums)            
        return ans            

        