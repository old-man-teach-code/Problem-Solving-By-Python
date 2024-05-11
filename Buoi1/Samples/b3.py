# Cho 1 mảng A có 20 phần tử số nguyên bất kỳ
# Sắp xếp mảng A tăng dần
import random
A = []
# Tạo 1 vòng lặp 20 lần lặp để thêm 20 phần tử ngẫu nhiên vào mảng A
for i in range(20):
    # Tạo 1 số ngẫu nhiên từ 0 đến 20
    ran_int = random.randint(0, 100)
    # Thêm số ngẫu nhiên vào mảng A
    A.append(ran_int)
print(A)
for i in range(20):
    for j in range(i+1,20):
        if(A[i]>A[j]):
            c = A[i]
            A[i] = A[j]
            A[j] = c
print(A)