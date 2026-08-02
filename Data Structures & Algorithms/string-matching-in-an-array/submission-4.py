class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        op = []
        for i in words:
            for j in words:
                if i != j:
                    if i in j:
                        op.append(i)
                        break
        return op