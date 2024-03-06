# 아래 함수를 수정하시오.
def even_elements(num_list):
    even_list = []
    for _ in range(len(num_list)):
        if num_list[0] % 2 == 0:
            even_list.append(num_list[0])
            num_list.pop(0)
        else: 
            num_list.pop(0)

    num_list.extend(even_list)
    return num_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)

