class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        op_str = ""
        for i in zip(*strs):
            if len(set(i)) > 1:
                return op_str
            op_str += i[0]
        return op_str
        