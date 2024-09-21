class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n=len(nums)
        c=0
        for i in range(n-1):
            for j in range(i+1,n):
                if(abs(nums[i]-nums[j])==k):
                    c+=1
        return c            


        