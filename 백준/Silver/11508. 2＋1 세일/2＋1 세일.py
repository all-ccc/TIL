n = int(input())
prices = [int(input()) for _ in range(n)]
prices.sort(reverse=True)   # 내림차순으로 정렬
discount = 0
# 정렬 후 가격들을 세 개씩 나눠서 봤을 때 세 번쨰에 오는 가격의 총합을 구할 거임
for i in range(2, n, 3):
    discount += prices[i]
    
# 원래 가격의 총합에서 할인 받은 값을 빼준다
print(sum(prices) - discount)