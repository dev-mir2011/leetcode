class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZero = 0  # pointer for placement of non-zeros

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZero], nums[i] = nums[i], nums[lastNonZero]
                lastNonZero += 1


# Time: O(n)
# Space: O(1)
