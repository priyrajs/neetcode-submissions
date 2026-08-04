class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = 0
        count = 0
        for i in nums:
            if i == 0:
                maxcount = max(maxcount,count)
                count = 0
            else:
                count += 1
        maxcount = max(maxcount,count)
        return maxcount
        