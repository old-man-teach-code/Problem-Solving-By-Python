def simple_hash_function(input_string: str) -> str:
    hash_value = 0
    for char in input_string:
        ascii_value = ord(char)
        hash_value = (hash_value * 31 + ascii_value) % (10**9 + 7)
    hashed_string = hex(hash_value)[2:]
    return hashed_string
input_string = "linh"
hashed_string = simple_hash_function(input_string)
print(f"Chuỗi gốc: {input_string}")
print(f"Chuỗi đã mã hóa: {hashed_string}")



