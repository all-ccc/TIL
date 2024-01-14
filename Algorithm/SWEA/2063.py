# 2063 중간값 찾기

# pass
a = int(input())
list_b = list(map(int, input().split()))
list_b.sort()
c = int(a // 2)
print (list_b[c])

# fail
a = int(input())
list_b = list(input().split())
list_b.sort()
c = int(a // 2)
print (list_b[c])

# fail 이유
# input().split()을 통해 입력된 숫자들을
# pass 코드는 공백으로 구분된 정수들을 입력받아 리스트로 저장
# fail 코드는 문자열을 입력받아 리스트로 저장
# 문자열 리스트일 경우 숫자를 오름차순으로 정렬해도 소용이 없음

