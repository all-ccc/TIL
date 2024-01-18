list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]

not_have_list = []

for rental in rental_list:
    if rental in list_of_book:
        continue
    else:
        not_have_list.append(rental)
        print(f'{rental} 은/는 보유하고 있지 않습니다.')
        break

# 다 있으면 우짤
if len(not_have_list) == 0:
    print('모든 도서가 대여 가능한 상태입니다.')



# 다른 방법

# for book in rental_list:
#     own = True
#     if book not in list_of_book:
#         print(f'{book} 은/는 보유하고 있지 않습니다.')
#         own=False
#         break
# if own:
#     print('모든 도서가 대여 가능한 상태입니다.')


# for else는 while else로도 가능. break로 정지조건 넣어서
    