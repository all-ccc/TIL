num = int(input())

for n in range(num):
    ox_list = list(input())
    score = 0
    score_result = 0
    for ox in ox_list:
        if ox == 'O':
            score += 1
            score_result += score
        else:
            score = 0
    print(score_result)