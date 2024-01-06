"""
Given two lists of intervals, find the intersection of these two lists. 
Each list consists of disjoint intervals sorted on their start time.

Example 1:

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.
Example 2:

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.
"""


class Interval:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f'[{str(self.start)}, {str(self.end)}]'


def solve(intervals_1: list[Interval], intervals_2: list[Interval]) -> list[Interval]:
    """
    To solve this: Merge Intervals
    We find the overlapped part
        start = max(a.start, b.start)
        end = min(a.end, b.end) 
    That is, the highest start time and the lowest end time will be the overlapping interval.

    So our algorithm will be to iterate through both the lists together to see if any two intervals overlap. 
    If two intervals overlap, we will insert the overlapped part into a result list and move on to the next
    interval which is finishing early.
    """
    ans: list[Interval] = []
    i, j = 0, 0
    while i < len(intervals_1) and j < len(intervals_2):
        first_overlaps_second = intervals_1[i].start >= intervals_2[
            j].start and intervals_1[i].start <= intervals_2[j].end

        second_overlaps_first = intervals_2[j].start >= intervals_1[
            i].start and intervals_2[j].start <= intervals_1[i].end

        if (first_overlaps_second or second_overlaps_first):
            ans.append(Interval(
                max(intervals_1[i].start, intervals_2[j].start),
                min(intervals_1[i].end, intervals_2[j].end)
            ))

        if intervals_1[i].end < intervals_2[j].end:
            i += 1
        else:
            j += 1
    print("Answer is: ", ans)
    return ans


assert [str(x) for x in solve([Interval(1, 3), Interval(5, 6), Interval(7, 9)], [Interval(
    2, 3), Interval(5, 7)])] == ['[2, 3]', '[5, 6]', '[7, 7]']
assert [str(x) for x in solve([Interval(1, 3), Interval(5, 7), Interval(9, 12)], [
    Interval(5, 10)])] == ['[5, 7]', '[9, 10]']


"""
Time complexity: O(N + M) where N and M are the lengths of the interval lists
Space complexity: S(1)
"""
