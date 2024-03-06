# 아래 함수를 수정하시오.
def sort_tuple(old_tuple):
    new_list = []
    old_list = list(old_tuple)
    old_list.sort()
    new_list.extend(old_list)
    new_tuple = tuple(new_list)
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
