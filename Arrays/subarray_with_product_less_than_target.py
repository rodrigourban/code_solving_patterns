from collections import deque
"""
Given an array with positive numbers and a target number, 
find all of its contiguous subarrays whose product is less than the target number.

Example 1:

Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.
Example 2:

Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target.
"""


def solve(nums: [int], target: int) -> [[int]]:
    """
    To solve this: Sliding window and Two Pointer
    This problem follows the Sliding Window and the Two Pointers pattern and shares 
    similarities with Triplets with Smaller Sum with two differences:

    In this problem, the input array is not sorted.
    Instead of finding triplets with sum less than a target, we need to find all subarrays having a product less than the target.
    The implementation will be quite similar to Triplets with Smaller Sum.
    """
    ans = []
    product = 1
    left = 0
    for right in range(len(nums)):
        product *= nums[right]
        while product >= target and left < len(nums):
            product /= nums[left]
            left += 1

        temp = deque()
        for i in range(right, left-1, -1):
            temp.appendleft(nums[i])
            ans.append(list(temp))

    print("Answer is: ", ans)
    return ans


assert solve([2, 5, 3, 10], 30) == [[2], [5], [2, 5], [3], [5, 3], [10]]
assert solve([8, 2, 6, 5], 50) == [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]]


"""
Time complexity: O(N^3)
Space complexity: S(N^2)
"""
