function solution(x, y, n) {
    const queue = [[x, 0]];
    const visited = Array(1000001).fill(false);
    visited[x] = true;
    let i = 0;

    while (i < queue.length) {
        const [now, count] = queue[i++];
        
        if (now === y) return count;
        
        for (let next of [now + n, now * 2, now * 3]) {
            if (next <= y && !visited[next]) {
                visited[next] = true;
                queue.push([next, count + 1]);
            }
        }
    }
    
    return -1;
}