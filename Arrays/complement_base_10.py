"""
Time complexity: O()
Space complexity: S()
"""

"""
Every non-negative integer N has a binary representation, for example, 
8 can be represented as “1000” in binary and 7 as “0111” in binary.

The complement of a binary representation is the number in binary that we get when we 
change every 1 to a 0 and every 0 to a 1. 
For example, the binary complement of “1010” is “0101”.

For a given positive number N in base-10, 
return the complement of its binary representation as a base-10 integer.

Example 1:

Input: 8
Output: 7
Explanation: 8 is 1000 in binary, its complement is 0111 in binary, which is 7 in base-10.
Example 2:

Input: 10
Output: 5
Explanation: 10 is 1010 in binary, its complement is 0101 in binary, which is 5 in base-10.
"""


def solve(num: int) -> int:
    """
    To solve this: XOR
    From the above-mentioned first property, we can conclude that XOR of a number with its 
    complement will result in a number that has all of its bits set to 1. For example, 
    the binary complement of “101” is “010”; and if we take XOR of these two numbers,
    we will get a number with all bits set to 1, i.e., 101 ^ 010 = 111
    We can write this fact in the following equation:
        number ^ complement = all_bits_set
    Let's add number on both sides:
        number ^ number ^ complement = number ^ all_bits_set
    From the above-mentioned second property:
        0 ^ complement = number ^ all_bits_set
    From the above-mentioned third property:
        complement = number ^ all_bits_set
    """
    bit_count, n = 0, num
    while n > 0:
        # to count number of bits
        # we shift left the most significant bit until it's 0
        bit_count += 1
        print(f"n {n:b}")
        n >>= 1

    # we can use the bit_count to find all_bits_set
    # all_bits_set = pow(2, bit_count) - 1
    all_bits_set = pow(2, bit_count) - 1

    print("Answer is: ", num ^ all_bits_set)
    # calculate and return the complement
    return num ^ all_bits_set


assert solve(8) == 7
assert solve(10) == 5


"""
Time complexity: O(b) b -> bits required to store num
Space complexity: S(1)
"""
