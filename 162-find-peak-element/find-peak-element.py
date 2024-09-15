class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # if(len(nums)==1 or nums[0]>nums[1]):
        #     return 0
        # if(nums[len(nums)-1]>nums[len(nums)-2]):
        #     return len(nums)-1
        # for i in range(1,len(nums)-1):
        #     if(nums[i]>nums[i-1] and nums[i]>nums[i+1]):
        #         return i 

        if(len(nums)==1 or nums[0]>nums[1]):
            return 0
        if(nums[len(nums)-1]>nums[len(nums)-2]):
            return len(nums)-1             
        l,h=1,len(nums)-2
        while(l<=h):
            mid=(l+h)>>1
            if(nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]):
                return mid 
            elif(nums[mid]<nums[mid+1]):
                l=mid+1
            else:
                h=mid-1                 