data = {
    '이름': '키위',
    '종류': '새',
    '원산지': '호주' 
}

plus_data = {
    '종류': '과일',
    '가격': 30000
}
# 1. data가 가진 모든 키와 벨류 목록을 출력한다.
# 가장 기본적인 dict 순회
for key in data:
    print(key, data[key])

# items() => [(key, value), (key, value)]
for item in data.items():
    print(item) # (key, value)
    key, value = item
    print(key, value)

# items() => [(key, value), (key, value)]
for key, value in data.items():
    print(key, value) # (key, value)

print(data.keys())
# for key in data:
# for key in data.keys():
#     print(key)



# 2. data가 가진 벨류 목록들만 모아서 출력한다.
print(data.values())

# 3. data에서 'without' 키가 가진 value를 출력한다.
    # 해당하는 키가 data에 없다면, 'unknown' 문자열을 출력한다.
# data가 가진 모든 값 순회
# for key in data:
#     # 순회도중 key의 값이 without이라면
#     if key == 'without':
#         # 근데 그 키가 있다면,
#         if data.get(key):
#             # value 출력
#             print(data[key])
#         # 없다면
#         else:
#             # 특정 문자열 출력
#             print('unknown')
print(data.get('without', 'unknown'))
    
# 4. plus_data가 가진 모든 키와 벨류를 data에 추가한다.
data.update(plus_data)
print(data.update(plus_data))
# for key in plus_data:
#     data[key] = plus_data[key]

# 5. 변경된 data를 출력한다.
print(data)
