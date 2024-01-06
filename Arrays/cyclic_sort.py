"""
We are given an array containing 'n' objects. Each object, when created, was assigned
a unique number from 1 to 'n' based on their creation sequence. This means that the object 
with sequence number '3' was created just before the object with sequence number '4'.

Write a function to sort the objects in-place on their creation sequence number in 
O(n) and without any extra space. For simplicity, let's assume we are passed an 
integer array containing only the sequence numbers, though each number is actually an object.

Example 1:

Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]
Example 2:

Input: [2, 6, 4, 3, 1, 5]
Output: [1, 2, 3, 4, 5, 6]
Example 3:

Input: [1, 5, 6, 4, 3, 2]
Output: [1, 2, 3, 4, 5, 6]
"""


def solve(lst: list[int]) -> list[int]:
    """
    To solve this: Cyclic Sort
    We iterate the array one number at a time, and if the current number we are iterating is
    not at the correct index, we swap it with the number at its correct index. This way we
    will go through all numbers and place them in their correct indices, hence, sorting the whole array.
    """
    i = 0
    while i < len(lst):
        # swap pair or increment i if correct in order
        if lst[i] == i + 1:
            i += 1
        else:
            new_value = lst[lst[i]-1]
            lst[lst[i] - 1] = lst[i]
            lst[i] = new_value
    return lst


assert solve([2, 6, 4, 3, 1, 5]) == [1, 2, 3, 4, 5, 6]
assert solve([3, 1, 5, 4, 2]) == [1, 2, 3, 4, 5]
assert solve([2, 6, 4, 3, 1, 5]) == [1, 2, 3, 4, 5, 6]
assert solve([1, 5, 6, 4, 3, 2]) == [1, 2, 3, 4, 5, 6]


"""
Time complexity: O(n)
Space complexity: O(1)
"""
