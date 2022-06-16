from DSA.Fibbonacci import Solution

def testFibbonacci():
    solution = Solution()
    
    # test case I 
    assert solution.fibbonacci(0) == 1

    # test case II
    assert solution.fibbonacci(7) == 13
