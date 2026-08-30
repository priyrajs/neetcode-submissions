class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def my_quicksort(nums2,p):
            n = len(nums2)
            if len(nums) == 1:
                return nums[0]
            pivot = nums2[n // 2]

            left = [x for x in nums2 if x < pivot]
            right = [x for x in nums2 if x > pivot]
            mid = [x for x in nums2 if x == pivot]

            l_right = len(right)
            l_mid = len(mid)

            if p <= l_right:
                return my_quicksort(right,p)
            elif p <= l_mid + l_right:
                return pivot
            else:
                return my_quicksort(left,p-l_right-l_mid)
        return my_quicksort(nums, k)
        