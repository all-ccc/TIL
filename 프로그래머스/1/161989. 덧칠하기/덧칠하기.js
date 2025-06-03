function solution(n, m, section) {
    let cnt = 0;
    let now = 0;
    
    for (let i = 0; i < section.length; i++) {
        if (now >= section[i]) {
            continue;
        }
        
        now = section[i] + m - 1;
        cnt++;
    }
    
    return cnt;
}