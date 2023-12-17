class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Time Complexity: O(nlogn)
        # basically the question is asking if there are any overlaps.
        # if there are no overlaps then the person can attend all the meetings 
        intervals.sort()
        
        #edge case
        if len(intervals) <= 1:
            return True  

        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False 
        return True 
                