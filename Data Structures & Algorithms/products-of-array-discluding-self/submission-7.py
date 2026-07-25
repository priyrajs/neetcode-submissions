class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #solution 1 is just a little bit space optimized version of this
        
        # prefix
        prefix_list = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            prefix_list[i] = prefix
            prefix *= nums[i]

        #postfix
        postfix_list = [1]*len(nums)
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            postfix_list[i] = postfix
            postfix *= nums[i]
        
        op = [1]*len(nums)

        # print(prefix_list,postfix_list)
        for j in range(len(op)):
            op[j] *= prefix_list[j]*postfix_list[j]
        return op
        

        