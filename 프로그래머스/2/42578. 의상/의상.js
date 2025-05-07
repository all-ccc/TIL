function solution(clothes) {
    const closet = {};

    for (let [item, category] of clothes) {
        if (!closet[category]) {
            closet[category] = 1;
        } else {
            closet[category]++;
        }
    }
    
    let result = 1;
    
    for (let category in closet) {
        result *= closet[category] + 1;
    }
    
    return result - 1;
    
}