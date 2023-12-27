"""
Given an array of n-1 integers in the range from 
1 to n, find the one number that is missing from the array.

Example:

Input: 1, 5, 2, 6, 4
Answer: 3
"""


def solve(lst: [int]) -> int:
    """
    To solve this:
    A straight forward approach to solve this problem can be:

    Find the sum of all integers from 1 to n; let's call it s1.
    Subtract all the numbers in the input array from s1; this will give us the missing number.

    While finding the sum of numbers from 1 to n, we can get integer overflow when n is large.

    XOR of a number with itself will always result in 0. This means that if we XOR all the 
    numbers in the input array with all numbers from the range 1 to n then each number in 
    the input is going to get zeroed out except the missing number. Following are the 
    set of steps to find the missing number using XOR:

    ^ is the XOR operator in Python

    1. XOR all the numbers from 1 to n, let's call it x1.
    2. XOR all the numbers in the input array, let's call it x2.
    3. The missing number can be found by x1 XOR x2.

    Important properties of XOR to remember #
    Following are some important properties of XOR to remember:

    Taking XOR of a number with itself returns 0, e.g.,

    1 ^ 1 = 0
    29 ^ 29 = 0
    Taking XOR of a number with 0 returns the same number, e.g.,

    1 ^ 0 = 1
    31 ^ 0 = 31
    XOR is Associative & Commutative, which means:

    (a ^ b) ^ c = a ^ (b ^ c)
    a ^ b = b ^ a
    Note: This solution could be optimized further by
    breaking from the cycle when we changes_made >= len(lst)
    """
    n = len(lst) + 1

    x1 = 1
    for i in range(2, n + 1):
        x1 ^= i

    x2 = lst[0]
    for i in range(1, n - 1):
        x2 ^= lst[i]

    return x1 ^ x2


assert solve([1, 5, 2, 6, 4]) == 3
assert solve([1, 5, 2, 6, 4, 3, 8]) == 7
assert solve([1, 5, 2, 6, 4, 3, 7, 8, 10, 11]) == 9


"""
Time complexity: O(n)
Space complexity: O(1)
"""
