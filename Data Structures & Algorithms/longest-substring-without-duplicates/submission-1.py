class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        strset = set()
        maxx = 0
        for r in range(len(s)):
            while s[r] in strset:
                strset.remove(s[l])
                l += 1
            strset.add(s[r])
            maxx = max(maxx, len(strset))
        return maxx