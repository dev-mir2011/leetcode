class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])

        return ans+nums


# Time Complexity: O(n)
# Space Complexity: O(n)
