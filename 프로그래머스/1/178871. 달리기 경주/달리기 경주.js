function solution(players, callings) {
    const rank = {};
    const names = [...players];
    
    players.forEach((player, index) => {
        rank[player] = index;
    })
    
    for (let player of callings) {
        let idx = rank[player];
        let frontPlayer = names[idx - 1];
        rank[frontPlayer]++;
        rank[player]--;
        
        [names[idx - 1], names[idx]] = [names[idx], names[idx - 1]];
    }
    
    return names;
}