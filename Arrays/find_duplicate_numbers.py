"""
We are given an unsorted array containing n+1 numbers taken from the range 1 to n. 
The array has only one duplicate but it can be repeated multiple times. Find that duplicate number 
without using any extra space. You are, however, allowed to modify the input array.

Example 1:

Input: [1, 4, 4, 3, 2]
Output: 4
Example 2:

Input: [2, 1, 3, 3, 5, 4]
Output: 3
Example 3:

Input: [2, 4, 1, 4, 4]
Output: 4
"""


def solve(nums: list[int]) -> int:
    """
    To solve this: Cyclic Sort
    Shares similarities with Find the Missing Number. Following a similar approach, 
    we will try to place each number on its correct index. Since there is only one duplicate,
    if while swapping the number with its index both the numbers being swapped are same, 
    we have found our duplicate!
    """
    ans = 0
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                # we swap them
                nums[i], nums[j] = nums[j], nums[i]
            else:
                ans = nums[i]
                break
        else:
            i += 1
    print("Answer is: ", ans)
    return ans


assert solve([1, 4, 4, 3, 2]) == 4
assert solve([2, 1, 3, 3, 5, 4]) == 3
assert solve([2, 4, 1, 4, 4]) == 4


"""
Time complexity: O(n)
Space complexity: S(1)
"""
