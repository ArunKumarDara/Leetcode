# n = a ^ 3
# n ^ 1/3 = a 
# if a ===  int 

class Solution:
    def isPowerOfThree(self, n: int) -> bool:  
        if n <= 0 :
            return False
        while n % 3 == 0:
            n /= 3 
        return n == 1
        