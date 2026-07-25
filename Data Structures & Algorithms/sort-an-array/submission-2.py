class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        mid = int(len(nums)/2)
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left,right)

    
    def merge(self,n1,n2):
        i,j = 0,0
        op_list = []
        while i < len(n1) and j < len(n2):
            if n1[i] < n2[j]:
                op_list.append(n1[i])
                i += 1
            else:
                op_list.append(n2[j])
                j += 1
        while i < len(n1):
            op_list.append(n1[i])
            i += 1
        while j < len(n2):
            op_list.append(n2[j])
            j += 1
        return op_list

        