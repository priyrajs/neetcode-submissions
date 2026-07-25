class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i in seen:
                seen[sorted_i].append(i)
            else:
                seen[sorted_i] = [i]
        op_list = []
        for i in seen:
            op_list.append(seen[i])
        return op_list

        