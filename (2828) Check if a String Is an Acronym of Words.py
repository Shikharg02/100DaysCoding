class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        c = 0
        if len(words) != len(s):
            return False
        for i in words:
            if i[0] != s[c]:
                return False
            c += 1
        return True
