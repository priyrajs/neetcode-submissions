class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        op = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                stc_in, stck_temp = stack.pop()
                op[stc_in] = i - stc_in
            stack.append((i, t))
        return op