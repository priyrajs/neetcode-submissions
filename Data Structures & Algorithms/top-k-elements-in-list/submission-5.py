class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in range(len(nums)+1):
            seen[i] = []
        
        seen2 = {}
        for j in nums:
            seen2[j] = seen2.get(j,0)+1
        
        for i in seen2:
            seen[seen2[i]].append(i)
        
        print(seen)
        op = []
        for i in range(len(seen)-1,-1,-1):
            print(i,seen[i],op)
            if len(seen[i])> 0:
                curr = 0
                while curr < len(seen[i]):
                    if len(op) == k:
                        return op
                    op.append(seen[i][curr])
                    curr += 1
                    
        return op
        