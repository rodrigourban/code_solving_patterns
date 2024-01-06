"""
Given a list of non-overlapping intervals sorted by their start time,
insert a given interval at the correct position and merge all necessary intervals to 
produce a list that has only mutually exclusive intervals.

Example 1:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
Example 2:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
Example 3:

Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
"""


class Interval:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f'[{str(self.start)}, {str(self.end)}]'


def solve(intervals: list[Interval], new_interval: Interval) -> list[Interval]:
    """
    To solve this: Merge Intervals
    1.Skip all intervals which end before the start of the new interval, i.e., 
    skip all intervals with the following condition:
        intervals[i].end < new_interval.start
    2.Let's call the last interval b that does not satisfy the above condition. 
    If b overlaps with the new interval (a) (i.e. b.start <= a.end), we need to
    merge them into a new interval c:
        c.start = min(a.start, b.start)
        c.end = max(a.end, b.end)
    3.We will repeat the above two steps to merge c with the next overlapping interval.
    """
    ans: list[Interval] = []
    i = 0
    while i < len(intervals) and intervals[i].end < new_interval.start:
        ans.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i].start <= new_interval.end:
        new_interval.start = min(intervals[i].start, new_interval.start)
        new_interval.end = max(intervals[i].end, new_interval.end)
        i += 1

    ans.append(new_interval)

    while i < len(intervals):
        ans.append(intervals[i])
        i += 1

    print("Answer is: ", ans)
    return ans


assert [str(x) for x in solve([Interval(1, 3), Interval(5, 7), Interval(8, 12)],
                              Interval(4, 6))] == ['[1, 3]', '[4, 7]', '[8, 12]']
assert [str(x) for x in solve([Interval(1, 3), Interval(5, 7), Interval(8, 12)],
                              Interval(4, 10))] == ['[1, 3]', '[4, 12]']
assert [str(x) for x in solve([Interval(2, 3), Interval(5, 7)],
                              Interval(1, 4))] == ['[1, 4]', '[5, 7]']


"""
Time complexity: O()
Space complexity: S()
"""
