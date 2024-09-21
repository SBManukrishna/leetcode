class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen=defaultdict(int)
        count=0
        for i in nums:
            t1,t2=i+k,i-k
            if t1 in seen:
                count+=seen[t1]
            if t2 in seen:
                count+=seen[t2]
            seen[i]+=1   
        return count          

        