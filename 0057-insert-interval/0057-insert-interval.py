class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Time Complexity: O(n)
        res = []
        
        for i in range(len(intervals)):
            # edge case -> to check if it overlapps 
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                # if newInterval is overlapping 
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    
        res.append(newInterval)

        return res 
