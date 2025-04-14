function solution(queue1, queue2) {
    const queue = [...queue1, ...queue2];
    const n = queue1.length;
    const maxCount = n * 3;
    
    const totalSum = queue.reduce((a, b) => a + b, 0);
    
    if (totalSum % 2 !== 0) return -1;
    
    const target = totalSum / 2;
    
    let count = 0;
    let start = 0;
    let end = n;
    let temp = queue1.reduce((a, b) => a + b, 0);
    
    while (count < maxCount) {
        if (temp === target) return count;
        
        if (temp < target) {
            temp += queue[end % (n * 2)];
            end++;
        } else {
            temp -= queue[start % (n * 2)];
            start++;
        }
        
        count++;
    }
    
    return -1;
}


