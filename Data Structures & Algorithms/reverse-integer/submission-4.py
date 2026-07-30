class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        a = abs(x)
        total = 0
        while a > 0:
            total *= 10
            total += a%10
            a //= 10
        total *= sign
        if total < -(1 << 31) or total > (1 << 31) - 1:
            return 0
        return total