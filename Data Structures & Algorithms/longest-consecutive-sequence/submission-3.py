class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(sorted(set(nums)))
        if not nums:
            return 0
        left=0
        right=1
        count=1
        maxi=1
        while right<len(nums):
            if nums[left]+1 == nums[right]:
                count+=1
                maxi=max(maxi,count)
            else:
                count=1
            left+=1
            right+=1
        return maxi

            

        