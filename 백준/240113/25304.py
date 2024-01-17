# 25304 영수증

total = int(input())
num = int(input())
shopping_sum = 0

for i in range(num):
    price, num = map(int, input().split())
    shopping_sum += price * num

if shopping_sum == total:
    print('Yes')
else:
    print('No')