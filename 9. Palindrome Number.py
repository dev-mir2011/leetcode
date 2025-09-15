class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        b = str(x)

        if b == b[::-1]:
            return True

        else:
            return False



# Time Complexity: O(d)
# Space Complexity: O(d)
