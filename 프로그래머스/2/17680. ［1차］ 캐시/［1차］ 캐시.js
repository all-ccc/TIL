function solution(cacheSize, cities) {
    let time = 0;
    const cache = [];
    
    for (let i = 0; i < cities.length; i++) {
        const now = cities[i].toLowerCase();
        let idx = cache.indexOf(now);
        
        if (idx < 0) { // cache miss
            if (cache.length >= cacheSize) {
                cache.pop();
            }
            
            if (cacheSize > 0) {
                cache.unshift(now);
            }
            time += 5;
        } else { // cache hit
            if (idx > 0) {
                cache.splice(idx, 1);
                cache.unshift(now);
            }
            time += 1;
        }
    }
    
    return time;
}