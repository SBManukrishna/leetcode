class Solution:
    def addDigits(self, num: int) -> int:
        while num:
            sum = 0
            while num:
                dig = num%10
                sum  += dig
                num //= 10
            if sum <10:
                return sum
            num = sum
        return 0
        
