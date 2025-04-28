function solution(lottos, win_nums) {
    let cnt = 0;
    let zero = 0;
    const rank = { '0': 6, '1': 6, '2': 5, '3': 4, '4': 3, '5': 2, '6': 1 };
    
    for (let i = 0; i < lottos.length; i++) {
        if (lottos[i] == 0) {
            zero++;
        }
        if (win_nums.includes(lottos[i])) {
            cnt++;
        }
    }
    
    let max = cnt + zero;
    let min = cnt;
    
    return [rank[max], rank[min]];
    
}