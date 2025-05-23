# Use a 1D DP array where dp[i] stores the number of combinations to make amount i.
# For each coin update dp from coin to amount to include combinations using that coin.
# This ensures each combination is counted only once per coin order.

# Time Complexity: O(amount * len(coins))
# Space Complexity: O(amount)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # use no coins

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]