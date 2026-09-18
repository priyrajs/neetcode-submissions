class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pivot = nums[n // 2]
        left = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        len_r = len(right)
        len_m = len(mid)

        if k <= len_r:
            return self.findKthLargest(right, k)
        elif k > len_r + len_m:
            return self.findKthLargest(left, k - len_m - len_r)
        else:
            return pivot