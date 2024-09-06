class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev=0
        curr=1
        for i in range(1,len(nums)):
            if(nums[i]==nums[prev]):
                if(i==len(nums)-1):
                    return curr
                pass
            else:
                nums[curr]=nums[i]
                prev+=1
                curr+=1
                if(i==len(nums)-1):
                    return curr
        print(nums)            
            
        