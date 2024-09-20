class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof=0
        mini=prices[0]
        for i in range(1,len(prices)):
            cost=prices[i]-mini
            prof=max(prof,cost)
            mini=min(mini,prices[i])
        return prof    

            
                
        