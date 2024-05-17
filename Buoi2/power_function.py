def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_power = power(a, n // 2)
        return half_power * half_power
    else:
        return a * power(a, n - 1)

# Testing the function
print(power(2, 10))  # 1024
