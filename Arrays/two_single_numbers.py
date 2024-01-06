"""
In a non-empty array of numbers, every number appears exactly twice except 
two numbers that appear only once. Find the two numbers that appear only once.

Example 1:

Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
Output: [4, 6]
Example 2:

Input: [2, 1, 3, 2]
Output: [1, 3]
"""


def solve(nums: list[int]) -> list[int]:
    """
    To solve this: XOR
    Let's assume num1 and num2 are the two single numbers. If we do XOR of all elements of 
    the given array, we will be left with XOR of num1 and num2 as all other numbers will
    cancel each other because all of them appeared twice. Let's call this XOR n1xn2. 
    1. Taking XOR of all numbers in the given array will give us XOR of num1 and num2, calling this XOR as n1xn2.
    2. Find any bit which is set in n1xn2. We can take the rightmost bit which is 1. Let's call this rightmost_bit.
    3. Iterate through all numbers of the input array to partition them into two groups based on rightmost_bit. 
    Take XOR of all numbers in both the groups separately. Both these XORs are our required numbers.
    """
    n1xn2 = 0
    for num in nums:
        # we calculate the XOR of every num in arr
        n1xn2 ^= num

    # get the rightmost bit that's 1
    rightmost_bit = 1
    while (rightmost_bit & n1xn2) == 0:
        # if not found, we shift left to check the next bit
        rightmost_bit <<= 1

    # iterate over array and classify nums based on rightmost_bit
    num1, num2 = 0, 0
    for num in nums:
        if (num & rightmost_bit) != 0:
            # bit is set
            num1 ^= num
        else:
            # bit is not set
            num2 ^= num

    print("Answer is: ", [num1, num2])
    return [num1, num2]


assert sorted(solve([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])) == [4, 6]
assert sorted(solve([2, 1, 3, 2])) == [1, 3]


"""
Time complexity: O(N)
Space complexity: S(1)
"""
