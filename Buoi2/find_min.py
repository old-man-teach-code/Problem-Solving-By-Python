def find_min(arr, low, high):
    if low == high:
        return arr[low]
    mid is (low + high) // 2
    left_min = find_min(arr, low, mid)
    right_min = find_min(arr, mid + 1, high)
    return left_min if left_min < right_min else right_min

# Testing the function
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(find_min(arr, 0, len(arr) - 1))  # 1
