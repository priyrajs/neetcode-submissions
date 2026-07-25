class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        op = ""
        while i < len(word1) and j < len(word2):
            op += word1[i] + word2[j]
            i ,j = i+1, j+1
        while i < len(word1):
            op += word1[i]
            i = i+1
        while j < len(word2):
            op += word2[j]
            j = j+1
        return op
        