import sys
sys.stdin = open('input.txt')

T = int(input())

for test in range(1, T+1):
    str1 = input()  # 길이가 N인 문자열
    str2 = input()  # 길이가 M인 문자열

    # 해당하는 문자가 몇 개 있는지를 딕셔너리에 넣어줌
    word_dict = {}

    for i in str1:  # str1의 글자 하나하나를 순회하면서
        if i in str2:   # 그 글자가 str2에 있다면
            word_dict.setdefault(i, str2.count(i))  # 해당 글자를 key로 하고 그 글자의 개수를 value로
    max_num = max(word_dict.values())   # value 값들 중 최댓값

    print(f'#{test} {max_num}')
