function solution(priorities, location) {
    let queue = priorities.map((priority, index) => [priority, index]);
    let count = 0;
    
    while (queue.length > 0) {
        let maxP = Math.max(...queue.map((value) => value[0]));
        let now = queue.shift();
        
        if (now[0] >= maxP) {
            count += 1;
            if (now[1] === location) {
                return count;
            }
        } else {
            queue.push(now);
        }
    }
}
