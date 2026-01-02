class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char = set()
        val = ""
        l = ""
        res = []
        if len(s)>1:
            for i in s:
                if i in char:
                    char.clear()
…        for i in res:
            if len(i) > count:
                count = len(i)
        return count