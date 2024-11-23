class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: Nin-place
        """
        ind = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break
        if ind == -1:
            nums[::] = nums[::-1]
            return nums
        for i in range(len(nums) - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                nums[ind + 1::] = nums[:ind:-1]
                return nums
