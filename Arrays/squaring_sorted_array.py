"""
Given a sorted array, 
create a new array containing squares of all the number of the input array in the sorted order.
Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]
"""


def solve(nums: [int]) -> []:
    """
    To solve this: Two pointers
    Since the numbers at both the ends can give us the largest square,
    an alternate approach could be to use two pointers starting at both the ends of the
    input array. At any step, whichever pointer gives us the bigger square we add it to 
    the result array and move to the next/previous number according to the pointer. 
    """
    ans = []
    x_pointer = len(nums) - 1
    y_pointer = 0
    while len(ans) != len(nums):
        if abs(nums[x_pointer]) >= abs(nums[y_pointer]):
            ans.insert(0, nums[x_pointer] ** 2)
            x_pointer -= 1
        else:
            ans.insert(0, nums[y_pointer] ** 2)
            y_pointer += 1

    print("Answer is: ", ans)
    return ans


assert solve([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9]
assert solve([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9]
assert solve([-6, -4, -3, -1, 0, 1, 2, 8]) == [0, 1, 1, 4, 9, 16, 36, 64]


"""
Time complexity: O(n)
Space complexity: S(n) Because len(output_array) = n
"""
