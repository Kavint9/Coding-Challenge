# Leetcode problem: https://leetcode.com/problems/insert-interval
# Time Complexity: O(N) - loop through intervals worst case
# Space Complexity: O(1)  


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        for i in range(len(intervals)):
            # newInterval Ends before the start of next interval - no overlap
            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                # if output inserted then the rest of the intervals can be appended
                return output + intervals[i:]
            # If new interval starts after the end of the current interval
            elif newInterval[0] > intervals[i][1]:
                # then append current interval
                output.append(intervals[i])
            # overlap between newInterval and the current Interval
            else:
                # Update New Interval
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]


        # if no interval exists with start after newInterval
        # code reaches this position
        # hence append new Interval
        output.append(newInterval)
        return output
