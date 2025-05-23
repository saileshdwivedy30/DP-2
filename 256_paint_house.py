# Use bottom up DP to track the minimum cost of painting each house with each color.
# For house i and color c add the min cost of painting house i-1 with a different color.
# Return the minimum cost of painting the last house with any of the three colors.

# Time Complexity: O(n)
# Space Complexity: O(1) — if done in-place on `costs`

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        n = len(costs)
        for i in range(1, n):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])  # paint red
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])  # paint blue
            costs[i][2] += min(costs[i-1][0], costs[i-1][1])  # paint green

        return min(costs[-1])  # min of last house painted any color
