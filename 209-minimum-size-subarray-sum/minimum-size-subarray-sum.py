class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        minlen=float('inf')
        sum=0
        for r in range(len(nums)):
            sum+=nums[r]

            while(sum>=target):
                minlen=min(minlen,r-l+1)
                sum-=nums[l]
                l+=1
        return minlen if minlen<float('inf') else 0       
            

