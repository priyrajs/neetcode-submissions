class Solution:
    def countBits(self, n: int) -> List[int]:
        op = []
        for i in range(n+1):
            bin = f"{i:b}"
            op.append(str(bin).count('1'))
        return op