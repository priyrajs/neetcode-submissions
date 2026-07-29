class Solution:
    def search(self, nums: List[int], target: int) -> int:
        seen = set(nums)
        if target not in seen:
            return -1
        return nums.index(target)
        