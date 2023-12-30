"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""


def solve(strings: str, k: int) -> int:
    """
    To solve this: Sliding Window
    We can use a HashMap to remember the frequency of each character we have processed. 
    Here is how we will solve this problem:

    1. First, we will insert characters from the beginning of the string until we have K 
    distinct characters in the HashMap.
    2. These characters will constitute our sliding window. We are asked to find the longest 
    such window having no more than K distinct characters. We will remember the length of this
    window as the longest window so far.
    3. After this, we will keep adding one character in the sliding window (i.e. slide the window ahead),
    in a stepwise fashion.
    4. In each step, we will try to shrink the window from the beginning if the count of distinct characters
    in the HashMap is larger than K. We will shrink the window until we have no more than K distinct characters
    in the HashMap. This is needed as we intend to find the longest window.
    5. While shrinking, well decrement the frequency of the character going out of the window and remove 
    it from the HashMap if its frequency becomes zero.
    5. At the end of each step, well check if the current window length is the longest so far, and if so,
    remember its length.
    """
    ans = 0
    window_start = 0
    frequency = {}
    for window_end in range(len(strings)):
        right_character = strings[window_end]
        if right_character not in frequency:
            frequency[right_character] = 0  # initialize

        frequency[right_character] += 1

        while len(frequency) > k:
            # shrink left
            left_character = strings[window_start]
            frequency[left_character] -= 1
            if frequency[left_character] == 0:
                del frequency[left_character]
            window_start += 1

        ans = max(ans, window_end - window_start + 1)

    return ans


assert solve("araaci", 2) == 4
assert solve("araaci", 1) == 2
assert solve("cbbebi", 3) == 5


"""
Time complexity: O(n + n) = O(n) outer + inner loop 
Space complexity: S(k) storing k+1 character in dict
"""
