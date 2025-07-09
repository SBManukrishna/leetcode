class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                tot = nums[l]+nums[r]+nums[i]
                if tot==0:
                    res.append([nums[l],nums[r],nums[i]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1        
                elif tot>0: 
                    r-=1
                else :
                    l+=1
        return  res            
        