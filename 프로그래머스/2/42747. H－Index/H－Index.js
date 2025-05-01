function solution(citations) {
    citations.sort((a, b) => b - a);
    
    let h = 1;
    
    for (let num of citations) {
        if (num >= h) {
            h++;
        } else {
            break;
        }
    }
    
    return h - 1;
}