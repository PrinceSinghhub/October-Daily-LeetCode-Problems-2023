from bisect import bisect_right, bisect_left


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start,end = [],[]
        for i,j in flowers:
            start.append(i)
            end.append(j)
        start.sort()
        end.sort()
        ans = []
        for i in people:
            ans.append(bisect_right(start,i)-bisect_left(end,i))
        return ans