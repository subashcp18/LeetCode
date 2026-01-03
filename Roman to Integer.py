class Solution:
    myDict = {"I": 1,"V": 5,"X":10,"L": 50,"C":100,"D":500,"M":1000}
    def romanToInt(self, s: str) -> int:
        lst = []
        nsum = 0
        for i in s:
            if i in self.myDict:
                lst.append(i)
            else:
                return -1
        i = 0
        while i < len(lst):
            f = lst[i]
            if i + 1 < len(lst) and self.myDict[f] < self.myDict[lst[i+1]]:
                nsum -= self.myDict[f]
            else:
                nsum += self.myDict[f]
            i+=1
        return nsum