class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        res=[]
        for i in range(n):
            sum=0
            if(k>=0):
                for j in range(1,k+1):
                    sum+=code[(i+j)%n]
            else:
                for j in range(1,abs(k)+1):
                    sum+=code[(i-j)%n]         
            res.append(sum)
        return res