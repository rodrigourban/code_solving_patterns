"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
one [1,5].
Example 2:

Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].
 
Example 3:

Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.
"""


class Interval:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f'[{str(self.start)}, {str(self.end)}]'


def solve(intervals: list[Interval]) -> list[Interval]:
    """
    To solve this: Merge Intervals
    1. Sort the intervals on the start time to ensure a.start <= b.start
    2. If 'a' overlaps 'b' (i.e. b.start <= a.end), we need to merge them into a new interval 'c' such that:
        c.start = a.start
        c.end = max(a.end, b.end)
    We will keep repeating the above two steps to merge 'c' with the next interval if it overlaps with 'c'.
    """
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x.start)
    merged: list[Interval] = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        if intervals[i].start <= end:
            # overlap, update end
            end = max(end, intervals[i].end)
        else:
            # not overlap, append interval c and advance start, end
            merged.append(Interval(start, end))
            start = intervals[i].start
            end = intervals[i].end

    # add last interval
    merged.append(Interval(start, end))
    return merged


assert solve([Interval(1, 4), Interval(2, 5), Interval(7, 9)]) == [
    [1, 5], [7, 9]]
assert solve([Interval(6, 7), Interval(2, 4), Interval(5, 9)]) == [
    [2, 4], [5, 9]]
assert solve([Interval(1, 4), Interval(2, 6), Interval(8, 11), Interval(
    10, 15), Interval(20, 22)]) == [[1, 6], [8, 15], [20, 22]]


"""
Time complexity: O(N*logN)
Space complexity: O(N)
"""
