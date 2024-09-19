class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=0-2**31
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            l=max(sum,l)
            if(sum<0):
                sum=0
        return l     




        