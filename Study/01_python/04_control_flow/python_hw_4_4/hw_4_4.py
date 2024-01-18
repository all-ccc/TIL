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

rental_book = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]

not_have_list = [rental for rental in rental_book if rental not in list_of_book]

# 똑같음
# not_have_list = []
# for rental in rental_book:
#     if rental not in list_of_book:
#         not_have_list.append(rental)

if len(not_have_list) == 0:
    print('모든 도서가 대여 가능한 상태입니다.')
else:
    for book in not_have_list:
        print(f'{book} 을/를 보충하여야 합니다')
