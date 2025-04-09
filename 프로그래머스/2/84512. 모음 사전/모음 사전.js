function solution(word) {
    let result = 0
    let count = 0;
    let isFound = false;
    const vowels = ['A', 'E', 'I', 'O', 'U'];
    
    makeWord('');
    
    return result;
    
    function makeWord(now) {
        if (now.length > 5 || isFound) return; // 길이 5 넘으면 유효 X
        
        if (now === word) {
            isFound = true;
            result = count;
            return;
        }
        
        count++;
        
        for (let v of vowels) {
            makeWord(now + v);
        }
        
    }
}