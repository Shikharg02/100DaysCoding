class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_set = set(nums)
        for num in num_set:
            count = nums.count(num)
            if count > len(nums) / 2:
                return num
