class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            dict[i]=target-nums[i]  
        for i in range(len(nums)):
            if dict[i] in nums and i!=nums.index(dict[i]):
                return [i,nums.index(dict[i])]    
        