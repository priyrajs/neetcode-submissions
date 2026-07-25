class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        op_list = set()
        i = 0
        while i <= len(nums)-1:
            if nums[i] in op_list:
                nums.pop(i)
            else:
                op_list.add(nums[i])
                i += 1
        return len(nums)

