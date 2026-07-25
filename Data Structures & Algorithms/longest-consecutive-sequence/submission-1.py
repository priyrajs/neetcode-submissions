class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest_seq = 0
        for i in nums:
            if i-1 not in seen:
                curr_num = i
                curr_seq = 1
                while curr_num+1 in seen:
                    curr_seq += 1
                    curr_num += 1
                longest_seq = max(longest_seq,curr_seq)
                
                    

        return longest_seq
                


        