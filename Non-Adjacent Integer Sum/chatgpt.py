def max_sum_non_adjacent(nums):
    if not nums:
        return 0
    
    n = len(nums)
    if n == 1:
        return nums[0]
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]

test = [2, 4, 6, 2, 5]
print(max_sum_non_adjacent(test))