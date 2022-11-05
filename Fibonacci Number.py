class Solution:
    def fib(self, n: int) -> int:
        """2 = f(1)+f(0)
          = 1 + 0 == 1
        3 = f(2)+f(1)
          = 1 + 1 == 2"""
        output = 0
        if n == 0:
            return 0
        if n == 1:
            return 1 
        output = self.fib(n-2) + self.fib(n-1)
        #print (output)
        return output
