class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Time Complexity: O(n.logn) 
        intervals.sort()

        res = 0 
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            # chechking for overlap 
            # this means they are not overlapping 
            if start >= prevEnd:
                prevEnd = end
            # else we have a overlap 
            else:
                res += 1 
                # while deleteing the intervals, we will keep the one that has the min end value
                prevEnd = min(end, prevEnd)
        return res 

