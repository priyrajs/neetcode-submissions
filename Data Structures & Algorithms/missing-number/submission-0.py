class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        all_nums = set([i for i in range(n+1)])
        res = list(all_nums-set(nums))
        return res[0]