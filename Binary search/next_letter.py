"""
Given an array of lowercase letters sorted in ascending order, 
find the smallest letter in the given array greater than a given key.

Assume the given array is a circular list, which means that the last letter
is assumed to be connected with the first letter. This also means that the smallest 
letter in the given array is greater than the last letter of the array
and is also the first letter of the array.

Write a function to return the next letter of the given key.

Example 1:

Input: ['a', 'c', 'f', 'h'], key = 'f'
Output: 'h'
Explanation: The smallest letter greater than 'f' is 'h' in the given array.
Example 2:

Input: ['a', 'c', 'f', 'h'], key = 'b'
Output: 'c'
Explanation: The smallest letter greater than 'b' is 'c'.
Example 3:

Input: ['a', 'c', 'f', 'h'], key = 'm'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.
Example 4:

Input: ['a', 'c', 'f', 'h'], key = 'h'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'h' is 'a'.
"""


def solve(letters: list[str], key: str) -> str:
    """
    To solve this: Binary Search
    We can use a similar approach as discussed in Ceiling of a Number. 
    There are a couple of differences though:

    The array is considered circular, which means if the key is bigger than 
    the last letter of the array or if it is smaller than the first letter of 
    the array, the key's next letter will be the first letter of the array.
    The other difference is that we have to find the next biggest letter which can't 
    be equal to the 'key'. This means that we will ignore the case where key == arr[middle]. 
    To handle this case, we can update our start range to start = middle +1.
    In the end, instead of returning the element pointed out by start, we have to return the
    letter pointed out by start % array_length. This is needed because of point 2 discussed above.
    Imagine that the last letter of the array is equal to the 'key'. 
    In that case, we have to return the first letter of the input array.
    """
    key_ord = ord(key)
    if ord(letters[-1]) <= key_ord or key_ord < ord(letters[0]):
        # since its circular, we know that if the last letter is less than equal to key,
        # the first if going to be the smallest letter greater than key
        # And if key is less than first element, first element is going to smaller greater
        print("Answer is: ", letters[0])
        return letters[0]

    start, end = 0, len(letters) - 1
    while start < end:
        middle = start + (end - start) // 2

        if ord(letters[middle]) > key_ord:
            end = middle

        if ord(letters[middle]) <= key_ord:
            start = middle + 1

    print("Answer is: ", letters[start])
    return letters[start]


assert solve(['a', 'c', 'f', 'h'], key='f') == 'h'
assert solve(['a', 'c', 'f', 'h'], key='b') == 'c'
assert solve(['a', 'c', 'f', 'h'], key='m') == 'a'
assert solve(['a', 'c', 'f', 'h'], key='h') == 'a'
assert solve(['c', 'f', 'h'], key='a') == 'c'


"""
Time complexity: O(logN)
Space complexity: S(1)
"""
