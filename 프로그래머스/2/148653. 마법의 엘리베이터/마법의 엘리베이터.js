function solution(storey) {
    let stone = 0;
    
    while (storey > 0) {
        let cur = storey % 10;
        let next = Math.floor(storey / 10) % 10;
        
        if (cur > 5 || (cur === 5 && next >= 5)) {
            storey += (10 - cur);
            stone += (10 - cur);
        } else {
            stone += cur;
            storey -= cur;
        }
        
        storey /= 10;
    }
    
    return stone;
}