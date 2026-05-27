class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict =  {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_dict:
                return sorted([i, my_dict[complement]])
            else:
                my_dict[nums[i]] = i
