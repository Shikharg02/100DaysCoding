class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        low = 0
        high = len(matrix) * len(matrix[0]) - 1

        while low <= high:
            mid = (low + (high - low) // 2)
            if target == matrix[mid // len(matrix[0])][mid % len(matrix[0])]:
                return True
            if target < matrix[mid // len(matrix[0])][mid % len(matrix[0])]:
                high = mid - 1
            if target > matrix[mid // len(matrix[0])][mid % len(matrix[0])]:
                low = mid + 1
        return False
