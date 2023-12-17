class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Time Complexity: O(nlogn)
        # this problem is mainly asking how many Overlaps are present 
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        
        res, count = 0, 0 
        
        s, e = 0, 0 
        
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1 
                count += 1
            else:
                #if end array is greater than the start array 
                #if the start and the end time is same then we will increment the 
                # e by 1 and decrement the count by 1 
                e += 1
                count -= 1
            res = max(res, count)
        return res 