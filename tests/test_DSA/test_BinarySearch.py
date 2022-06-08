from DSA.BinarySearch import Solution

def testBinarySearch():
    solution = Solution()
    test_cases = [[[-1, 0, 3, 5, 9, 12], 5, 3], [[-1, 0, 3, 5, 9, 12], 2, -1]] # [nums, target, result]
    
    for nums, target, result in test_cases:
        low = 0
        high = len(nums) - 1
        assert solution.binarySearch(nums, target, low, high) == result