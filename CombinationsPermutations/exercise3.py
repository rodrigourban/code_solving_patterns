"""
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}
If a set has 'n' distinct elements it will have n! permutations.
Input: [1,3,5]
Output: [[5, 3, 1], [3, 5, 1], [3, 1, 5], [5, 1, 3], [1, 5, 3], [1, 3, 5]]
"""


def solve(lst: [int]) -> [[]]:
    """
    To solve this: Breadth First Search (BFS) but all permutations have to contain every number
    Let's take the example-1 mentioned above to generate all the permutations. Following a BFS approach, we will consider one number at a time:

    1. If the given set is empty then we have only an empty permutation set: []
    2. Let's add the first element (1), the permutations will be: [1]
    3. Let's add the second element (3), the permutations will be: [3,1], [1,3]
    4. Let's add the third element (5), the permutations will be: [5,3,1], [3,5,1], [3,1,5], [5,1,3], [1,5,3], [1,3,5]
    5. Let's analyze the permutations in the 3rd and 4th step. How can we generate permutations in the 4th step from the permutations of the 3rd step?

    If we look closely, we will realize that when we add a new number (5), we take each permutation of the previous step and insert
    the new number in every position to generate the new permutations. For example, inserting '5' in different positions of [3,1] 
    will give us the following permutations:

    1. Inserting '5' before '3': [5,3,1]
    2. Inserting '5' between '3' and '1': [3,5,1]
    3. Inserting '5' after '1': [3,1,5]
    """
    permutations = [[lst[0]]]
    for number in range(1, len(lst)):
        new_permutations = []
        for subarray in permutations:
            for i in range(0, len(subarray)+1):
                new = subarray.copy()
                new.insert(i, lst[number])
                new_permutations.append(new)
        permutations = new_permutations

    return permutations


print(solve([1, 3, 5]))

assert solve([1, 3, 5]) == [[5, 3, 1], [3, 5, 1], [
    3, 1, 5], [5, 1, 3], [1, 5, 3], [1, 3, 5]]

"""
Time complexity: O(N * N!)
Space complexity: O(N * N!)
"""
