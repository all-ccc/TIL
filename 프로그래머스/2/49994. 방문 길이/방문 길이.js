function solution(dirs) {
    const dx = [0, 0, -1, 1]; // 상하좌우
    const dy = [1, -1, 0, 0];
    const dirMap = { 'U' : 0, 'D' : 1, 'L' : 2, 'R' : 3 };
    
    let x = 0, y = 0; // 현재 좌표
    const visited = new Set();
    
    let count = 0;
    
    for (let dir of dirs) {
        let i = dirMap[dir];
        let nx = x + dx[i];
        let ny = y + dy[i];
        
        let path = `${x}, ${y} - ${nx}, ${ny}`;
        let reversePath = `${nx}, ${ny} - ${x}, ${y}`;
        
        if (nx > 5 || nx < -5 || ny > 5 || ny < -5) continue;
        
        // 방문한 적 없는 길이면 set에 이동 좌표 추가하기 / count 하기
        if (!visited.has(path) && !visited.has(reversePath)) { // 양방향 모두 확인해야 함 !!
            visited.add(path); // 저장은 한 방향만 해도 됨
            count++;
        }
        
        // 현재 좌표 갱신해주기
        x = nx;
        y = ny;
        
    }
    
    return count;
}