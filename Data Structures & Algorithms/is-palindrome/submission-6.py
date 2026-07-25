class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer method
        filtered_s = ''.join(list(filter(lambda x:x.isalnum(),s))).lower()
        l = 0
        r = len(filtered_s)-1
        print(filtered_s)

        while r > l:
            if filtered_s[l] != filtered_s[r]:
                return False
            l += 1
            r -= 1
        return True


        