def sum_array(arr, low, high):
    if low > high:
        return 0
    elif low == high:
        return arr[low]
    else:
        mid = (low + high) // 2
        left_sum = sum_array(arr, low, mid)
        right_sum = sum_array(arr, mid + 1, high)
        return left_sum + right_sum

# Testing the function
arr = [1, 2, 3, 4, 5]
print("Tổng các phần tử:", sum_array(arr, 0, len(arr) - 1))  # 15
