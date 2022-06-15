from DSA.TwoSum import Solution

def testTwoSum():
    solution = Solution()
    
    # testcase I:
    # Input: nums = [-3,4,3,90], target = 0
    # Output: [0, 2]
    assert solution.twoSum([-3,4,3,90], 0) == (0, 2)
    
    # test cases II:
    # Input: nums = [3, 2, 4], target = 6
    # output = (1, 2)
    assert solution.twoSum([3, 2, 4], 6) == (1, 2)