class Solution(object):
    def maxProfit(self, prices):
        length = len(prices)
        maxprofit = 0
        for epoch in prices:
            for i in range(prices.index(epoch)+1, length):
                if prices[i] - epoch > maxprofit:
                    maxprofit = prices[i] - epoch
        if maxprofit > 0:
            return maxprofit
        else:
            return 0         # 超时

    def maxProfit2(self, prices):
        if len(prices) == 0:
            return 0
        else:
            maxprofit = 0
            minprice = prices[0]
            for epoch in prices:
                if epoch < minprice:
                    minprice = epoch
                maxprofit = max(maxprofit, epoch-minprice)
            return maxprofit       # 限制买卖一次

    def maxPrifit3(self, prices):
        if len(prices) == 0:
            return 0
        else:
            maxprofit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    maxprofit += prices[i] - prices[i-1]
        return maxprofit            # 无限次数，只要是递增序列都可以相加

a = Solution()
print(a.maxPrifit3([1,2,3,4,5,6]))