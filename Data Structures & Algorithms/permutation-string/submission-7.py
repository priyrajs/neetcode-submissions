class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        seen = {}
        for i in s1:
            seen[i] = seen.get(i,0)+1
        
        r = n
        for l in range(len(s2)):
            str1 = s2[l:r]
            seen1 = {}
            for j in str1:
                seen1[j] = seen1.get(j, 0) + 1
            if seen == seen1:
                return True
            r += 1
        return False

