class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for item in nums:
           if item in dict and dict[item] > 0:
            return True
           else:
            dict[item] = dict.get(item, 0) + 1
        return False