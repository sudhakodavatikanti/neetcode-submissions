class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for num in nums:
            if num in my_dict and my_dict[num] > 0:
                return True

            my_dict[num] = my_dict.get(num, 0) + 1

        return False