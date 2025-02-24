function solution(s) {
    let result = s.length;

    for (let i = 1; i <= Math.floor(s.length / 2); i++) {
        let idx = 0;
        let word = '';
        let count = 1;
        
        while (idx < s.length) {
            let curr = s.slice(idx, idx + i);
            let next = s.slice(idx + i, idx + 2*i);
            
            if (curr === next) {
                count += 1;
            } else {
                if (count > 1) word += count;
                word += curr;
                count = 1;
            }
            idx += i;
        }
        // console.log(word);
        result = Math.min(word.length, result);
    }
    
    return result;
    
}