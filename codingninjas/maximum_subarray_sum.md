Kadane's algorithm is a dynamic programming algorithm used to find the maximum subarray sum in a given array. The algorithm works by maintaining two variables: `max_so_far` and `max_ending_here`. `max_so_far` stores the maximum sum of subarray found so far, while `max_ending_here` stores the maximum sum of subarray ending at the current index. The algorithm iterates through the array and updates these variables as follows:

1. Set `max_so_far` and `max_ending_here` to the first element of the array.
2. For each subsequent element in the array, update `max_ending_here` to the maximum of either the current element or the sum of the current element and `max_ending_here`.
3. If `max_ending_here` is greater than `max_so_far`, update `max_so_far` to `max_ending_here`.
4. Return `max_so_far`.

Here is an example implementation of the algorithm in Python:

```python
def kadane(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
```

Let's do a dry run of this algorithm on the input array `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`:

1. `max_so_far` and `max_ending_here` are both initialized to `-2`.
2. The next element is `1`, so `max_ending_here` is updated to `1`.
3. The next element is `-3`, so `max_ending_here` is updated to `-2`.
4. The next element is `4`, so `max_ending_here` is updated to `4`.
5. The next element is `-1`, so `max_ending_here` is updated to `3`.
6. The next element is `2`, so `max_ending_here` is updated to `5`.
7. The next element is `1`, so `max_ending_here` is updated to `6`.
8. The next element is `-5`, so `max_ending_here` is updated to `1`.
9. The final element is `4`, so `max_ending_here` is updated to `5`.
10. The maximum subarray sum is `6`.

I hope this helps!