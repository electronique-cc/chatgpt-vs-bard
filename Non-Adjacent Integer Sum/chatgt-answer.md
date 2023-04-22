Here's one possible implementation of the program in Python:
```python
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
```

The idea behind this solution is to use dynamic programming to keep track of the maximum sum that can be obtained by adding any non-adjacent integers up to a certain index i in the input list. We initialize a dynamic programming array `dp` of length n (the length of the input list), where `dp[i]` represents the maximum sum that can be obtained by adding any non-adjacent integers up to index i.

We then use the following recurrence relation to compute `dp[i]` for each index i:

```python
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

This recurrence relation says that we can either skip the current number and use the maximum sum we have computed up to the previous index `i-1`, or we can add the current number to the maximum sum we have computed up to the index two positions before `i-2`. We take the maximum of these two options as the maximum sum up to index i.

We can then return the last element of the dynamic programming array `dp` as the maximum sum that can be obtained by adding any non-adjacent integers in the input list.

This algorithm has a time complexity of O(n), where n is the length of the input list, since we need to iterate over the input list once and perform constant-time operations at each step.