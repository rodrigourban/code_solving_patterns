"""
Find the maximum value in a given Bitonic array. 
A bitonic array is a sorted array; the only difference is that its first 
part is sorted in ascending order and the second part is sorted in descending order.
arr[i] != arr[i+1]

Example 1:

Input: [1, 3, 8, 12, 4, 2]
Output: 12
Explanation: The maximum number in the input bitonic array is '12'.
Example 2:

Input: [3, 8, 3, 1]
Output: 8
Example 3:

Input: [1, 3, 8, 12]
Output: 12
Example 4:

Input: [10, 9, 8]
Output: 10
"""


def solve(nums: list[int]) -> int:
    """
    To solve this: Binary Search
    Since no two consecutive numbers are same (as the array is monotonically increasing or decreasing), 
    whenever we calculate the middle, we can compare the numbers pointed out by the 
    index middle and middle+1 to find if we are in the ascending or the descending part. So:
    1.If arr[middle] > arr[middle + 1], we are in the second (descending) part of the bitonic array. 
    Therefore, our required number could either be pointed out by middle or will be before middle. 
    This means we will be doing: end = middle.
    2.If arr[middle] <= arr[middle + 1], we are in the first (ascending) part of the bitonic array. 
    Therefore, the required number will be after middle. This means we will be doing: start = middle + 1.
    We can break when start == end. Due to the two points mentioned above, both start and end 
    will be pointing at the maximum number of the bitonic array.
    """
    start = 0
    end = len(nums) - 1
    while start < end:
        middle = start + (end - start) // 2

        if nums[middle] > nums[middle + 1]:
            end = middle
        elif nums[middle] <= nums[middle + 1]:
            start = middle + 1

    print("Answer is: ", start)
    return nums[start]


assert solve([1, 3, 8, 12, 4, 2]) == 12
assert solve([3, 8, 3, 1]) == 8
assert solve([1, 3, 8, 12]) == 12
assert solve([10, 9, 8]) == 10


"""
Time complexity: O(logN)
Space complexity: S(1)
"""
