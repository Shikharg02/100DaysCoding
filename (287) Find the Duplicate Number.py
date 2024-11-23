class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtypertype: int
        """
        nums.sort()
        x = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == x:
                return x
            else:
                x = nums[i]
