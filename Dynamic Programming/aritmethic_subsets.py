from collections import defaultdict
"""
Arithmetic Slices II - Subsequence

Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.

 

Example 1:

Input: nums = [2,4,6,8,10]
Output: 7
Explanation: All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
Example 2:

Input: nums = [7,7,7,7,7]
Output: 16
Explanation: Any subsequence of this array is arithmetic.
 

Constraints:

1  <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1    

To get combinations without repeated you do
(n * ( n - 1 ) ) // 2
"""


"""
Old solution 
for i in range(0, n - 2):
    for j in range(i + 1, n - 1):  # 3
        current_set = set()
        current_diff = nums[j] - nums[i]
        current_set.add(nums[j])
        for x in range(j + 1, n):
            if nums[x] - current_diff in current_set:
                count += 1
                current_set.add(nums[x])
"""


def arithmetic_subsets(nums: list[int]) -> int:
    # store length for later use
    count, n = 0, len(nums)

    if n < 3:
        # not arithmetic
        return 0

    dp = [defaultdict(int) for _ in range(n)]

    for i in range(n):

        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] += 1 + dp[j][diff]
            count += dp[j][diff]

    print("Count is: ", count)
    return count


assert arithmetic_subsets(nums=[2, 4, 6, 8, 10]) == 7
assert arithmetic_subsets(nums=[7, 7, 7, 7, 7]) == 16
assert arithmetic_subsets(nums=[7, 7, 7]) == 1
assert arithmetic_subsets(nums=[7, 7, 7, 7]) == 5
assert arithmetic_subsets([79, 20, 64, 28, 67, 81, 60, 58, 97, 85, 92, 96, 82, 89, 46, 50, 15, 2, 36, 44, 54, 2, 90, 37, 7, 79, 26, 40, 34, 67, 64, 28, 60, 89, 46, 31, 9, 95, 43, 19, 47, 64, 48, 95, 80, 31, 47, 19, 72,
                           99, 28, 46, 13, 9, 64, 4, 68, 74, 50, 28, 69, 94, 93, 3, 80, 78, 23, 80, 43, 49, 77, 18, 68, 28, 13, 61, 34, 44, 80, 70, 55, 85, 0, 37, 93, 40, 47, 47, 45, 23, 26, 74, 45, 67, 34, 20, 33, 71, 48, 96]) == 1030
