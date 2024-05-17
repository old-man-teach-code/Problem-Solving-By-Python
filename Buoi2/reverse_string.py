def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])

# Testing the function
s = "hello"
print(reverse_string(s))  # "olleh"
