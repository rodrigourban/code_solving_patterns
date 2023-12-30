"""
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
"""


def solve(strings: str) -> int:
    """
    To solve this: Sliding Window
    This problem follows the Sliding Window pattern and we can use a similar dynamic 
    sliding window strategy as discussed in Longest Substring with K Distinct Characters. 
    We can use a HashMap to remember the last index of each character we have processed. 
    Whenever we get a repeating character we will shrink our sliding window to ensure that
    we always have distinct characters in the sliding window.
    """
    ans = 0
    window_start = 0
    frequency = {}
    for window_end in range(len(strings)):
        right_character = strings[window_end]

        if right_character in frequency:
            window_start = max(window_start, frequency[right_character] + 1)

        frequency[right_character] = window_end
        ans = max(ans, window_end - window_start + 1)

    print("Answer is: ", ans)
    return ans


assert solve("aabccbb") == 3
assert solve("abbbb") == 2
assert solve("abccde") == 3


"""
Time complexity: O(n)
Space complexity: S(k) -> but since we are expecting only 26 letters we could say S(1)
"""
