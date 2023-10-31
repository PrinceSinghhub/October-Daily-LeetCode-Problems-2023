from typing import List
from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        sz = len(nums)
        dp, queue = [0] * sz, deque()
        dp[-1] = nums[-1]
        queue.append(sz - 1)
        for idx in range(sz - 2, -1, -1):
            if queue[0] - idx > k:
                queue.popleft()
            dp[idx] += (nums[idx] + dp[queue[0]])
            dp[idx] = max(dp[idx], nums[idx])
            while queue and dp[idx] > dp[queue[-1]]:
                queue.pop()
            queue.append(idx)
        return max(dp)