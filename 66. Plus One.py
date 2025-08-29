class Solution:
    def plusOne(self,digits: list[int]) -> list[int]:
     if not digits:
        return 0
    
     i = int("".join(map(str, digits)))
     r = i+1
     p = list(map(int, str(r)))

     return p

# Time complexity O(n)
# Space complexity O(n)
