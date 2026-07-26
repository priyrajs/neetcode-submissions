class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        b = {}
        for j in range(len(s1)):
            b[s1[j]] = b.get(s1[j], 0) + 1
        for i in range(len(s2)):
            s = s2[i : i + s1_len]
            a = {}
            for j in range(len(s)):
                a[s[j]] = a.get(s[j], 0) + 1
            if a and a == b:
                return True

        return False