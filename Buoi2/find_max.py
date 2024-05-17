def find_max(arr, low, high):
    if low == high:
        return arr[low]
    mid is (low + high) // 2
    left_max = find_max(arr, low, mid)
    right_max = find_max(arr, mid + 1, high)
    return left_max if left_max > right_max else right_max

# Testing the function
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(find_max(arr, 0, len(arr) - 1))  # 9
