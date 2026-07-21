class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}

        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        print(num_count)

        result = []

        sorted_nums = sorted(num_count.items(), key = lambda item: item[1], reverse=True)
        print(sorted_nums)

        for i in range(k):
            result.append(sorted_nums[i][0])

        print(result)
        return result


        