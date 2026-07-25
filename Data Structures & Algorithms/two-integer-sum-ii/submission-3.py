class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(numbers)):
            remain = target-numbers[i]
            if remain in seen:
                return [seen[remain],i+1]
            else:
                seen[numbers[i]] = i+1
                


        