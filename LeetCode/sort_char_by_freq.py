# 451: Sort Characters by Frequency

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        charDict = {}
        newDict = {}
        newStr = ""

        for ch in range(len(s)):
            if s[ch] not in charDict: charDict[s[ch]] = 0
            charDict[s[ch]] += 1

        for key in charDict:
            if charDict[key] in newDict:
                newDict[charDict[key]].append(key * charDict[key])
            else:
                newDict[charDict[key]] = [key*charDict[key]]

        order = sorted(newDict.keys())

        for rank in reversed(order):
            newStr += "".join(newDict[rank])

        return newStr


from collections import Counter

# more elegant solution from LeetCode

class Solution(object):
    def frequencySort(self, s: str) -> str:
        counter1, counter2 = Counter(s), {}
        newStr = ""

        for key, val in counter1.items():
            counter2.setdefault(val, []).append(key*val)

        for idx in range(len(s), -1, -1):
            if idx in counter2:
                newStr += "".join(counter2[idx])

        return newStr
