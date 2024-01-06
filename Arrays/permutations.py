"""
Given a set of distinct numbers, find all of its permutations.
Permutation is defined as the re-arranging of the elements of the set. 
For example, {1, 2, 3} has the following six permutations:
{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}
If a set has n distinct elements it will have 
n! permutations.

Example 1:
Input: [1,3,5]
Output: [[5, 3, 1], [3, 5, 1], [3, 1, 5], [5, 1, 3], [1, 5, 3], [1, 3, 5]]
"""


def solve(nums: list[int]) -> list[int]:
    """
    To solve this:  Breadth First Search (BFS)
    Let's take the example-1 mentioned above to generate all the permutations. 
    Following a BFS approach, we will consider one number at a time:
    If the given set is empty then we have only an empty permutation set: []
    Let's add the first element (1), the permutations will be: [1]
    Let's add the second element (3), the permutations will be: [3,1], [1,3]
    Let's add the third element (5), the permutations will be: [5,3,1], [3,5,1], [3,1,5], [5,1,3], [1,5,3], [1,3,5]
    Let's analyze the permutations in the 3rd and 4th step.
    How can we generate permutations in the 4th step from the permutations of the 3rd step?

    If we look closely, we will realize that when we add a new number (5), 
    we take each permutation of the previous step and insert the new number in every position to generate the new 
    permutations. For example, inserting 5 in different positions of [3,1] will give us the following permutations:

    Inserting 5 before 3: [5,3,1]
    Inserting 5 between 3 and 1: [3,5,1]
    Inserting 5 after 1: [3,1,5]
    """
    ans: list[list[int]] = [[nums[0]]]
    for i in range(1, len(nums)):
        sub_array: list[list[int]] = []
        for sub in ans:
            for j in range(len(sub)+1):
                new_permutation = sub.copy()
                new_permutation.insert(j, nums[i])
                sub_array.append(new_permutation)
        ans = sub_array

    print("Answer is: ", ans)
    return ans


assert sorted(solve([1, 3, 5])) == [[1, 3, 5], [1, 5, 3], [
    3, 1, 5], [3, 5, 1], [5, 1, 3], [5, 3, 1]]


"""
Time complexity: O(N*N!)
Space complexity: S(N*N!)
"""
