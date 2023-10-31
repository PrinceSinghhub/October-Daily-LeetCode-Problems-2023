import math


class Solution:
    def isPowerOfFour(self, num):
        if (num <= 0):
            return False

        # n = math.log(num)
        # n1 = math.log(4)



        return ((math.log(num) / math.log(4)).is_integer())

ans = Solution()
n = 16
print(ans.isPowerOfFour(n))
