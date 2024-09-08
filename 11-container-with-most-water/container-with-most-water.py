class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        maxarea=min(height[l],height[r])*(r-l)
        while(l!=r):
            if(height[l]>height[r]):
                r-=1
            else:
                l+=1
            area=min(height[l],height[r])*(r-l)
            if(area>maxarea):
                maxarea=area        
        return maxarea


        

        