class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in range(len(nums)+1):
            seen[i] = []
        
        seen2 = {}
        for j in nums:
            seen2[j] = seen2.get(j,0)+1
        
        for num,count in seen2.items():
            seen[count].append(num)
        
        op = []
        for i in range(len(seen)-1,0,-1):
            for res in seen[i]:
                op.append(res)
                if len(op) == k:
                    return op
        