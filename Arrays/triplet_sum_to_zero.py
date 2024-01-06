"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
"""


def search_pair(nums: [int], target_sum: int, left: int) -> [[int]]:
    triplets = []
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target_sum:
            triplets.append([-target_sum, nums[left], nums[right]])
            left += 1
            right -= 1

            # skip duplicates
            while nums[left] == nums[left-1]:
                left += 1
            while nums[right] == nums[right + 1]:
                right -= 1

        elif target_sum > current_sum:
            # we need a bigger pair
            left += 1
        else:
            # we need a smaller pair
            right -= 1

    return triplets


def solve(nums: [int]) -> [[int]]:
    """
    To solve this: Two pointers
    First, we will sort the array and then iterate through it taking one number at a time. 
    Let's say during our iteration we are at number X, so we need to find Y and Z such that 
    X+Y+Z==0. At this stage, our problem translates into finding a pair whose sum is equal to
    -X (as from the above equation Y+Z==-X).

    Another difference from Pair with Target Sum is that we need to find all the unique triplets. 
    To handle this, we have to skip any duplicate number. Since we will be sorting the array, 
    so all the duplicate numbers will be next to each other and are easier to skip.
    """
    sorted_array = sorted(nums)
    ans = []

    for i in range(len(sorted_array)):
        if sorted_array[i] > 0 or sorted_array[i] == sorted_array[i-1]:
            continue

        ans.extend(search_pair(sorted_array, -sorted_array[i], i+1))

    print("Answer is: ", ans)
    return ans


assert solve([-3, 0, 1, 2, -1, 1, -2]) == [[-3, 1, 2],
                                           [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
assert solve([-5, 2, -1, -2, 3]) == [[-5, 2, 3], [-2, -1, 3]]


"""
Time complexity: O(N^2) -> Sorting array: N*logN, search_pair = N -> N^2
Space complexity: S(N)
"""
