import math
"""
Given an array of unsorted numbers and a target number, 
find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet.
If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
Example 2:

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
Example 3:

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
"""


def solve(nums: [int], target: int) -> int:
    """
    To solve this:
    """
    sorted_array = sorted(nums)
    smallest_sum = math.inf
    for i in range(len(sorted_array)-2):
        left = i + 1
        right = len(sorted_array) - 1
        while left < right:
            target_sum = sorted_array[i] + \
                sorted_array[left] + sorted_array[right]

            if abs(target - target_sum) < abs(target - smallest_sum):
                smallest_sum = target_sum

            if target_sum > target:
                right -= 1
            else:
                left += 1

    print("Answer is: ", smallest_sum)
    return smallest_sum


assert solve([-2, 0, 1, 2], 2) == 1
assert solve([-3, -1, 1, 2], 1) == 0
assert solve([1, 0, 1, 1], 100) == 3


"""
Time complexity: O(N^2)
Space complexity: S(1)
"""
