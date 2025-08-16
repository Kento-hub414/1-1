def knapsack_cost_only(num_items, max_cost, items):
    
    dp = [[0] * (max_cost + 1) for _ in range(num_items + 1)]

    for i in range(num_items):
        w, v, c = items[i]
        for cost in range(max_cost + 1):
            # 入れない
            dp[i+1][cost] = max(dp[i+1][cost], dp[i][cost])
            # 入れる
            if cost - c >= 0:
                dp[i+1][cost] = max(dp[i+1][cost], dp[i][cost - c] + v)

    return dp[num_items][max_cost]

if __name__ == "__main__":
    n, W, C = map(int, input().split())
    items = []
    for _ in range(n):
        w, v, c = map(int, input().split())
        items.append((w, v, c))

    print(knapsack_cost_only(n, C, items))