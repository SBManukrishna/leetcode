class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if(nums[i]!=0):
                pass
            else:
                j=i+1
                while(j<len(nums)-1 and nums[j]==0):
                    j+=1 
                nums[j],nums[i]=nums[i],nums[j]  

        