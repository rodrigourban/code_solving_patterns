"""
Given an array arr of unsorted numbers and a target sum, count all triplets in it such that 
arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.
Write a function to return the count of such triplets.

Example 1:

Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
Example 2:

Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
"""


def search_pair(nums: [int], target: int, first: int) -> [int]:
    count = 0
    left = first + 1
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] < target:
            # since arr[right] > arr[left], any number below right is going to
            # be less than target.
            count += right - left
            # if we wanted the triplets instead we would
            # for i in range(right, left, -1): triplets.append([nums[start], nums[left], nums[right]])
            left += 1
        else:
            right -= 1
    return count


def solve(nums: [int], target: int) -> int:
    """
    To solve this: Two pointers
    Shares similarities with Triplet Sum to Zero. The only difference is that, 
    in this problem, we need to find the triplets whose sum is less than the given target. 
    To meet the condition i != j != k we need to make sure that each number is not used more than once.
    Following a similar approach, first we can sort the array and then iterate through it, 
    taking one number at a time. Let's say during our iteration we are at number X, 
    so we need to find Y and Z such that
    X+Y+Z<target. At this stage, our problem translates into finding a pair whose sum is less than “$target - X$”
    (as from the above equation Y+Z==target-X). We can use a similar approach as discussed in Triplet Sum to Zero.
    """
    sorted_array = sorted(nums)
    ans = 0
    for i in range(len(sorted_array)-2):
        ans += search_pair(sorted_array, target-sorted_array[i], i)

    print("Answer is: ", ans)
    return ans


assert solve([-1, 0, 2, 3], 3) == 2
assert solve([-1, 4, 2, 1, 3], 5) == 4


"""
Time complexity: O(N^2)
Space complexity: S(N)
"""
