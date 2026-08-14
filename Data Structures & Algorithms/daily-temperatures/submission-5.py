class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        op = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, stackIn = stack.pop()
                op[stackIn] = i - stackIn
            stack.append([t, i])
        return op
            
        