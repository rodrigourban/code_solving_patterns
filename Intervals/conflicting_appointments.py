"""
Given an array of intervals representing N appointments, find out if a person can attend all the appointments.

Example 1:

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
Example 2:

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.
Example 3:

Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.
"""


class Interval:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f'[{str(self.start)}, {str(self.end)}]'


def solve(intervals: list[Interval]) -> bool:
    """
    To solve this: Merge Intervals
    The problem follows the Merge Intervals pattern. 
    We can sort all the intervals by start time and then check if any two intervals overlap. 
    A person will not be able to attend all appointments if any two appointments overlap.
    """
    ordered_intervals = sorted(intervals, key=lambda x: x.start)

    end = ordered_intervals[0].end

    for i in range(1, len(ordered_intervals)):
        if ordered_intervals[i].start <= end:
            # overlap found, cannot attend to all appointments
            print("Answer is:", False)
            return False
        end = ordered_intervals[i].end

    print("Answer is: ", True)
    return True


assert solve([Interval(1, 4), Interval(2, 5), Interval(7, 9)]) == False
assert solve([Interval(6, 7), Interval(2, 4), Interval(8, 1)]) == True
assert solve([Interval(4, 5), Interval(2, 3), Interval(3, 6)]) == False


"""
Time complexity: O(N*logN) because of sorting
Space complexity: S(N) because of sorting
"""
