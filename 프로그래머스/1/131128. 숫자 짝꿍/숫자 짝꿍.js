function solution(X, Y) {
    const xCount = new Array(10).fill(0);
    const yCount = new Array(10).fill(0);
    let result = '';
    
    for (let num of X) {
        xCount[num] += 1;
    }
    for (let num of Y) {
        yCount[num] += 1;
    }

    for (let i = 9; i >= 0; i--) {
        result += i.toString().repeat(Math.min(xCount[i], yCount[i]));
    }

    if (result === '') return '-1';
    if (result[0] === '0') return '0';

    return result;
}
