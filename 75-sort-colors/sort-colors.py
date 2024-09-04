class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # res=[nums[0]]
        # curr=0
        # for i in range(1,len(nums)):
        #     if(nums[i]>res[curr]):
        #         res.append(nums[i])
        #         curr+=1
        c0,c1,c2=0,0,0
        # dict1={0:0,1:0,2:0}
        for i in range(len(nums)):
            match nums[i]:
                case 0:
                    c0+=1
                case 1:
                    c1+=1
                case 2:
                    c2+=1
        l0=[0]*c0
        l1=[1]*c1
        l2=[2]*c2
        res=l0+l1+l2
        for i in range(len(nums)):
            nums[i]=res[i]                     
            