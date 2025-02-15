function solution(s){
    let count = 0;
    
    for (let str of s) {
        if (str === '(') {
            count += 1;
        } else {
            count -= 1;
        }
        
        if (count < 0) return false;
    }
    
    return count === 0;
}