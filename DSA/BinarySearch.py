
class Solution(object):

    """
Binary Search: algorithm to find an item's position from a sorted list of items.
Binary search can be solved using recursive or iterative method.

Here, the solution is applied using Recursive method

test case 1
nums = [-1, 0, 3, 5, 9, 12]
target = 9
result = 4

test case 2
nums = [-1, 0, 3, 5, 9, 12]
target = 2
result = -1
"""

    
    def binarySearch(self, nums, target, low, high):
        
        if low <= high:  # check if lower index exceed higher, in that case, target is not available in the array/list
            mid = int((low + high)/2)
            mid_value = nums[mid]

            if target == mid_value:
                return mid
            elif target < mid_value:
                self.low = low
                self.high = mid - 1
                return self.binarySearch(nums, target, self.low, self.high)

            else:
                self.low = mid + 1
                self.high = high
                return self.binarySearch(nums, target, self.low, self.high)
        
        return -1
