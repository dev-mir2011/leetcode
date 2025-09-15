class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        st = s.lower()
        if st == st[::-1]:
            return True

        else:
            return False


# Time: O(n)
# Space: O(n)
