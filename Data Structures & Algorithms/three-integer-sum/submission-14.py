class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, v in enumerate(nums):

            if (
                i > 0 and v == nums[i - 1]
            ):  # here checking value of v should not be same to avoid repeating values
                continue

            l = i + 1
            r = len(nums) - 1

            while r > l:
                total = v + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1  # we will do this bcoz we need to increase either l or r
                    while (
                        l < r and nums[l] == nums[l - 1]
                    ):  # also checking l should be in range and value of l index should not be same
                        l += 1

        return res
                
