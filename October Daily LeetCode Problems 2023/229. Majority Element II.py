class Solution:

    def majorityElementApprioch3(self,n,nums):

        Min = len(nums) // 3
        ans = []

        count1 = 0
        ele1 = -10**9

        count2 = 0
        ele2 = -10**9

        for i in range(n):

            if count1 == 0 and nums[i] != ele2:
                count1 = 1
                ele1 = nums[i]

            elif count2 == 0 and nums[i] != ele1:
                count2 = 1
                ele2 = nums[i]

            elif nums[i] == ele1:
                count1+=1

            elif nums[i] == ele2:
                count2+=1

            else:
                count1-=1
                count2-=1

        # now reIterate in the array and check if the element == arr[i] then incremetn the our both cout

        count1 = 0
        count2 = 0

        for i in range(n):

            if ele1 == nums[i]:
                count1+=1

            if ele2 == nums[i]:
                count2+=1

        # check if the couts > then / 3 or not

        if count1 > Min:
            ans.append(ele1)
        if count2 > Min:
            ans.append(ele2)

        return ans

    def majorityElement(self, nums):

        N = len(nums)
        ans = self.majorityElementApprioch3(N,nums)

        return ans

ans = Solution()
arr = [1,1,1,1,3,2,2,2]
print(ans.majorityElement(arr))
