class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        
        return False
    


# Time complexity O(n Log n)
# Space comlexity O(1) average, O(n) worst
