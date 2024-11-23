class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: int
        """

        x, y, z = len(s1), len(s2), len(s3)
        m = min(x, y, z)
        c, i = False, 0

        if s1[0] != s2[0] or s1[0] != s3[0]:
            return -1

        for i in range(1, m):
            if s1[i] != s2[i] or s1[i] != s3[i]:
                c = True
                break

        if c:
            return (x - i) + (y - i) + (z - i)
        else:
            return (x - i - 1) + (y - i - 1) + (z - i - 1)
