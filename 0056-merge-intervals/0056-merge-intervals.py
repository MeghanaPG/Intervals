class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time Complexity: O(n.logn)
        intervals.sort(key = lambda i:i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                # we will have to merge then 
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start,end])
        return output 

    