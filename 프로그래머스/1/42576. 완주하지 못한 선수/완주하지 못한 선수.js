function solution(participant, completion) {
    let playerMap = new Map(); 
    for (let name of participant) {
        // 맵에 저장 안되어있으면 1 넣고 저장 되어있으면 기존 값에 1 더해주기
        if (playerMap.has(name)) {
            playerMap.set(name, playerMap.get(name) + 1);
        } else {
            playerMap.set(name, 1);
        }
    }
    
    for (let com of completion) {
        playerMap.set(com, playerMap.get(com) - 1);
    }
    
    for (let [key, value] of playerMap) {
        if (value >= 1) {
            return key;
        }
    }
}