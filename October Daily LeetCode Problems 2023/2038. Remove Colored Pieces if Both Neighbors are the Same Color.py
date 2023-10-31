class Solution:
    def winnerOfGame(self, arr: str) -> bool:
        n = len(arr)

        def count(char):
            i, j = 0, 0
            res = 0
            while j < n:
                temp = 0
                while j < n and arr[j] == char:
                    temp += 1
                    j += 1

                res += (temp - 2) if temp > 2 else 0
                j += 1
                i = j
            return res

        return count('A') > count('B')