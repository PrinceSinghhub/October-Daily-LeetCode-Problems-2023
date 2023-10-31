class Solution:
    def passsgenerateRow(self, n):
        ans = 1
        result = [ans]

        for i in range(1, n):
            # for numerator
            ans *= (n - i)
            # for denominator
            ans //= i
            result.append(ans)

        return result

    def getRow(self, rowIndex):
        return self.passsgenerateRow(rowIndex + 1)
