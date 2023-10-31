class Solution:

    def searchRange(self, nums, target):

        ans = [-1,-1]
        start = self.findIndex(nums,target,True)
        end = self.findIndex(nums,target,False)

        ans[0] = start
        ans[1] = end
        return ans

    def findIndex(self, nums, target, boolean):

        start = 0
        end = len(nums) - 1

        ans = -1

        while (start <= end):
            mid = start + (end - start) // 2

            if (target > nums[mid]):
                start = mid + 1

            if (target < nums[mid]):
                end = mid - 1

            if(target == nums[mid]):
                ans = mid
                if(boolean==True):
                    end = mid-1
                else:
                    start = mid+1
        return ans


