class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def my_quick_sort(arr, k):
            n = len(arr)
            pivot = arr[n // 2]

            left = [x for x in arr if x < pivot]
            mid = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]

            len_r = len(right)
            len_m = len(mid)

            if k <= len_r:
                return my_quick_sort(right, k)
            elif k <= (len_m + len_r):  # k = 3,r=2, m = 2
                return pivot
            else:
                return my_quick_sort(left, k - len_r - len_m)

        return my_quick_sort(nums, k)