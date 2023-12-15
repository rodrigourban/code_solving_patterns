"""
Given a string, find all of its permutations preserving the character sequence but changing case.

Example 1:

Input: "ad52"
Output: ["ad52", "Ad52", "aD52", "AD52"]
Example 2:

Input: "ab7c"
Output: ["ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"]
"""


def solve(lst: [int]) -> []:
    """
    To solve this: Breadth First Search (BFS) approach
    Following a BFS approach, we will consider one character at a time. 
    Since we need to preserve the character sequence, we can start with the actual string and process each
    character (i.e., make it upper-case or lower-case) one by one:

    1. Starting with the actual string: "ab7c"
    2. Processing the first character ('a'), we will get two permutations: "ab7c", "Ab7c"
    3. Processing the second character ('b'), we will get four permutations: "ab7c", "Ab7c", "aB7c", "AB7c"
    4. Since the third character is a digit, we can skip it.
    5. Processing the fourth character ('c'), we will get a total of eight permutations: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
    """
    permutations = [lst]
    for i in range(0, len(lst)):
        if (lst[i].isalpha()):
            to_append = []
            for substr in permutations:
                to_append.append(
                    f'{substr[0:i]}{substr[i].swapcase()}{substr[i+1:]}')
            permutations.extend(to_append)

    return permutations


assert solve("ad52") == ["ad52", "Ad52", "aD52", "AD52"]
assert solve("ab7c") == ["ab7c", "Ab7c", "aB7c",
                         "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"]


"""
Time complexity: O(N * 2^N)
Space complexity: O(N * 2^N)
"""
