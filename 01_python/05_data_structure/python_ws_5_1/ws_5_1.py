# 아래 함수를 수정하시오.
def reverse_string(str):
    str_list = list(str)
    str_list.reverse()
    string = ''.join(str_list)
    return string


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
