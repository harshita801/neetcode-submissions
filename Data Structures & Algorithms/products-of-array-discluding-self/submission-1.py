class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[1]*n
        left_product=1
        right_product=1
        for i in range(n):
            ans[i]*=left_product
            left_product*=nums[i]

            ans[n-1-i]*=right_product
            right_product*=nums[n-1-i]
        return ans