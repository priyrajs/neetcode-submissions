class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op_list = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            op_list[i] = prefix
            prefix *= nums[i]
            

        postfix = 1
        for j in range(len(nums)-1,-1,-1):
            op_list[j] *= postfix
            postfix *= nums[j]
            


        return op_list

        