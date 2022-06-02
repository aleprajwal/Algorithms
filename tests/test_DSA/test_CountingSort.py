from DSA.CountingSort import Solution

def testCountingSort():
    solution = Solution()
    assert solution.countingSort([3,5,6,3,2,1,2]) == [1,2,2,3,3,5,6]