class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        stored_numbers = {}  # number -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in stored_numbers:
                return [stored_numbers[complement], i]
            stored_numbers[num] = i

        return []
# Two Sum Solution

