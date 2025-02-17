function solution(begin, target, words) {
    if (!words.includes(target)) return 0;
    
    function checkWord(word1, word2) { // 다른 알파벳 개수 체크하는 함수
        let count = 0;
        for (let i = 0; i < word1.length; i++) {
            if (word1[i] !== word2[i]) count ++;
            if (count > 1) return false;
        }
        return count === 1;
    }
    
    const queue = [[begin, 0]];
    const visited = {}; // 방문한 단어 저장
    visited[begin] = true;
    
    while (queue.length > 0) {
        const [nowWord, step] = queue.shift();
        
        if (nowWord === target) return step;
        
        for (word of words) {
            if (checkWord(nowWord, word) && !visited[word]) {
                queue.push([word, step + 1]);
                visited[word] = true;
            }
        }
        
    }
    
    return 0;
}