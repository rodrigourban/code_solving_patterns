"""
Given an array of characters where each character represents a fruit tree, 
you are given two baskets and your goal is to put maximum number of fruits in each basket. 
The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can't skip a tree.
You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""


def solve(fruits: [str]) -> int:
    """
    To solve this: Sliding Window
    This problem is quite similar to Longest Substring with K Distinct Characters.
    In this problem, we need to find the length of the longest subarray with no more than two 
    distinct characters (or fruit types!). This transforms the current problem into Longest 
    Substring with K Distinct Characters where K=2.
    """
    ans = 0
    baskets = 2
    window_start = 0
    frequency = {}
    for window_end in range(len(fruits)):
        right_character = fruits[window_end]
        if right_character not in frequency:
            frequency[right_character] = 0

        frequency[right_character] += 1

        while len(frequency) > baskets:
            left_character = fruits[window_start]
            frequency[left_character] -= 1
            if frequency[left_character] == 0:
                del frequency[left_character]

            window_start += 1

        ans = max(ans, window_end - window_start + 1)

    print("Answer is: ", ans)
    return ans


assert solve(['A', 'B', 'C', 'A', 'C']) == 3
assert solve(['A', 'B', 'C', 'B', 'B', 'C']) == 5


"""
Time complexity: O()
Space complexity: S()
"""
