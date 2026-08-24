class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        sorted_intervals = sorted(intervals)
        
        result = [sorted_intervals[0].copy()]

        for current_interval in sorted_intervals[1:]:
            last_merged = result[-1]


            if last_merged[1] >= current_interval[0]:
                last_merged[1] = max(last_merged[1], current_interval[1])

            else:
                result.append(current_interval.copy())

        return result
        