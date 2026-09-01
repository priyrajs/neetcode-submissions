class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ls = [str(x) for x in nums]
        numstr = "".join(ls)
        res = []
        for i in numstr.split('0'):
            res.append(len(i))
        return max(res)