
class Factorial():
    """Calculation of a factorial using recursion concept"""
    
    def factorials(self, n:int()):
        if n >= 0:
            if n == 0:
                return 1
            return n * self.factorials(n-1)
