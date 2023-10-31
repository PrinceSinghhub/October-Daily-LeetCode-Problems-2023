class Solution:
    def sortByBits(self, arr):
        arr = [(bin(i).count('1'), i) for i in arr]
        print(arr)
        arr.sort()

        ans = []

        for i in arr:
            ans.append(i[1])

        return ans