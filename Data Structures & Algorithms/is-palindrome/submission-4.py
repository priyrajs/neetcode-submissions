class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(list(filter(lambda x:(x.isalnum()), s))).lower()
        # print(cleaned)
        # if len(cleaned) <= 1:
        #     return False
        return cleaned == cleaned[::-1]
        