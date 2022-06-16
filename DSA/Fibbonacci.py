
class Solution():
    """
    returns fibbonacci number of nth place
    fibbonacci series = 1,1,2,3,5,8,13,...
    case I: fibbonacci(0) = 1
    case II: fibbonacci(7) = 13
    

    Python3 implementation of Fibbonacci sequence
    Use of Recursion technique
    """

    def fibbonacci(self, n:int()):
        if n <= 2:
            return 1
        
        return self.fibbonacci(n-1) + self.fibbonacci(n-2)

