class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        ret, i, j = 0, k, k
        while i >= 0 or j < len(nums):
            lvl = max(nums[i] if i >= 0 else 0, nums[j] if j < len(nums) else 0)
            while i >= 0 and nums[i] >= lvl:
                i -= 1
            while j < len(nums) and nums[j] >= lvl:
                j += 1
            ret = max(ret, (j - i - 1) * lvl)
        return ret
