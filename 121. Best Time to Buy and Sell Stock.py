class Solution:
    def maxProfit(self, prices: List[int]) -> int:
     l, r = 0, 1
     mp = 0

     while r < len(prices):

         if prices[l] < prices[r]:
             profit = prices[r] - prices[l]
             mp = max(mp, profit)

         else:
             l = r
         r += 1
    
     return mp

# Time complexity O(n)
# Space complexity O(1)
