function solution(k, m, score) {
    let result = 0;
    score.sort((a, b) => b - a); // 내림차순
    
    for (let i = 1; i * m - 1 < score.length; i++){
        result += score[i * m - 1] * m;
    }
    
    return result;
}