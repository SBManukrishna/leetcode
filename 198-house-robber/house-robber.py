class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+1)
        def helper(i):
            if i==0:
                dp[0]=nums[0]
                return dp[0]
            if(i==1):
                dp[1]=max(nums[0],nums[1])
                return dp[1]
            if(dp[i]!=-1):
                return dp[i]
            dp[i]=max(nums[i]+helper(i-2),helper(i-1))  
            return dp[i]       
        return helper(n-1)             
