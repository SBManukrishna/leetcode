class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=0-2**31
        sum=0
        for i in nums:
            sum+=i
            l=max(sum,l)
            if(sum<0):
                sum=0
        return l     




        