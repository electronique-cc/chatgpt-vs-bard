Sure, here is the program in Python:

```python
def max_non_adjacent_sum(list):
  """Returns the maximum sum that can be obtained by adding any non-adjacent integers in the list."""

  # Check if the list is empty.
  if not list:
    return 0

  # Initialize the maximum sum and the current sum.
  max_sum = 0
  current_sum = 0

  # Iterate over the list.
  for i in range(len(list)):
    # If the current element is not adjacent to the previous element, add it to the current sum.
    if i > 0 and list[i] != list[i - 1]:
      current_sum += list[i]

    # Update the maximum sum.
    max_sum = max(max_sum, current_sum)

  # Return the maximum sum.
  return max_sum
```

This program has a time complexity of O(n), where n is the length of the input list. The reason is that we only need to iterate over the list once, and we only need to do constant-time operations at each iteration.