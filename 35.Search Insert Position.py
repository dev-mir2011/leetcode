class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        if target in nums:
            if len(nums) == 1:
                return 0
                
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        

        elif target not in nums:
            nums.append(target)
            nums.sort()

        
            for i in range(len(nums)):
                 if nums[i] == target:
                      return i


# Time complexity O(n) if found, O(n log n) if not found
# Space complexity O(1) average, O(n) worst case
