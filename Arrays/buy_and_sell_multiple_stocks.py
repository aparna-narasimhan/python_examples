#Input: [7,1,5,3,6,4]
#Output: 7 => 1 to 5 + 3 to 6
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return(profit)

s = Solution()
max_profit = s.maxProfit([7,1,5,3,6,4])
print(max_profit)