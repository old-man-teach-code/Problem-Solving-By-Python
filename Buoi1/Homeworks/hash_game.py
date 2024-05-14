import time

# Hàm check_password(input_password: str) -> bool nhận vào một chuỗi input_password và trả về True nếu chuỗi đúng mật khẩu
def check_password(input_password: str) -> bool:
    hashed_password = simple_hash_function(input_password)
    if hashed_password == "1075eeff":
        return True
    return False


def simple_hash_function(input_string: str) -> str:
    hash_value = 0
    for char in input_string:
        ascii_value = ord(char)
        hash_value = (hash_value * 31 + ascii_value) % (10**9 + 7)
    hashed_string = hex(hash_value)[2:]
    return hashed_string

def find_password():
    password = "abcdef"
    # TODO: Viết hàm tìm ra mật khẩu
    check_password(password)
    if check_password(password):
        print("Mật khẩu đúng")
        return password
    else:
        print("Sai mật khẩu")
        return ""

def main():
    # process time calculation 
    start = time.time()
    print("----------------------------")
    password = find_password()
    print(f"Mật khẩu cần tìm là: {password}")
    end = time.time()
    print(f"Thời gian chạy: {end - start} giây")
    print("----------------------------")


if __name__ == '__main__':
    main()



