class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        
        if val in nums:
            for i in range(nums.count(val)):
                nums.remove(val)

    
        return len(nums)


# Time complexity O(n²)
# Space complexity O(1)
