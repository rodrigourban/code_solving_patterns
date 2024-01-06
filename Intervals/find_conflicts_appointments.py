"""
Problem 1: Given a list of appointments, find all the conflicting appointments.

Example:

Appointments: [[4,5], [2,3], [3,6], [5,7], [7,8]]
Output: 
[4,5] and [3,6] conflict. 
[3,6] and [5,7] conflict.
"""


class Interval:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f'[{str(self.start)}, {str(self.end)}]'


def solve(intervals: list[Interval]) -> list[list[Interval]]:
    """
    To solve this: Merge Intervals
    The problem follows the Merge Intervals pattern. 
    We can sort all the intervals by start time and then check if any two intervals overlap. 
    A person will not be able to attend all appointments if any two appointments overlap.
    """

    intervals.sort(key=lambda x: x.start)
    ans: list[list[Interval]] = []
    start_interval = intervals[0]

    for i in range(1, len(intervals)):
        if intervals[i].start < start_interval.end:
            # overlap, update end
            ans.append([Interval(start_interval.start, start_interval.end), Interval(
                intervals[i].start, intervals[i].end)])

            if start_interval.end < intervals[i].end:
                # check which interval is larger
                start_interval = intervals[i]
            continue
        start_interval = intervals[i]

    print("Answer is: ", ans)
    return ans


assert [str(x) for x in solve([Interval(4, 5), Interval(2, 3), Interval(3, 6),
                               Interval(5, 7), Interval(7, 8)])] == ['[[3, 6], [4, 5]]', '[[3, 6], [5, 7]]']


"""
Time complexity: O(N*logN) because of sorting
Space complexity: S(N) because of sorting
"""
