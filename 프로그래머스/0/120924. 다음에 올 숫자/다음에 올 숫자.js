function solution(common) {
    let [a, b, c] = common;
    let result = common[common.length - 1];

    if (b / a === c / b) {
        result *= (b / a);
    } else {
        result += (b - a);
    }
    
    return result;
}