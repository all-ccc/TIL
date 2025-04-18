function solution(array, commands) {
    const num = commands.length;
    const result = [];
    
    for (let n = 0; n < num; n++) {
        let [i, j, k] = commands[n];
        const newArr = array.slice(i - 1, j);
        
        newArr.sort((a, b) => (a - b));
        result.push(newArr[k - 1]);
    }
        
    return result;
}