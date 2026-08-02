class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        op = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                elif words[i] in words[j]:
                    op.append(words[i])
                    break
        return op