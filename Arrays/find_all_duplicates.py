"""
We are given an unsorted array containing n numbers taken from the range 1 to n. 
The array has some duplicates, find all the duplicate numbers without using any extra space.

Example 1:

Input: [3, 4, 4, 5, 5]
Output: [4, 5]
Example 2:

Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]
"""


def solve(nums: list[int]) -> list[int]:
    """
    To solve this: Cyclic Sort
    Shares similarities with Find the Duplicate Number. Following a similar approach, 
    we will place each number at its correct index. After that, we will iterate through
    the array to find all numbers that are not at the correct indices. 
    All these numbers are duplicates.
    """
    ans: list[int] = []
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            ans.append(nums[i])

    print("Answer is: ", ans)
    return ans


assert sorted(solve([3, 4, 4, 5, 5])) == [4, 5]
assert sorted(solve([5, 4, 7, 2, 3, 5, 3])) == [3, 5]


"""
Time complexity: O()
Space complexity: S()
"""
