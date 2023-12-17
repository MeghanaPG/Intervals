class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Time Complexity: O(nlogn + qlogq)
        intervals.sort()

        minHeap = []
        # res is a hashmap which we will convert it into a list later 
        # i refers to the index of the initial interval
        res, i = {}, 0 
        for q in sorted(queries):
            # traverse through the intervals 
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                # heap with (size,right_val)
                heapq.heappush(minHeap, (r-l+1, r))
                i += 1 

            #now we have to remove the intervals that the q doesn't belong to 
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1 
        
        return [res[q] for q in queries]


        