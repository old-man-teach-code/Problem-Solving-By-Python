n = int(input("n = "))
def so_chinh_phuong(n):
    for i in range(n):
        if(i * i == n):
            return True
    return False
if(so_chinh_phuong(n)):
    print("Yes")
else:
    print("No")