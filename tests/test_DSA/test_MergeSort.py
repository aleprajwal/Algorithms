from DSA.MergeSort import Solution

def testMergeSort():
    solution = Solution()
    arr = [4,3,5,7,6,9,8,2]
    solution.mergeSort(arr)
    assert  arr == [2,3,4,5,6,7,8,9]