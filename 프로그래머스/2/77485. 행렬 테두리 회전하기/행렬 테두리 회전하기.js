function solution(rows, columns, queries) {
    const result = [];
    const map = Array.from({length: rows + 2}, () => Array(columns + 2).fill(0));
    
    let num = 1;
    for (let i = 1; i <= rows; i++) {
        for (let j = 1; j <= columns; j++) {
            map[i][j] = num++;
        }
    }
    
     for (let [sx, sy, ex, ey] of queries) {
        const stack = [];
         
        for (let y = sy; y < ey; y++) stack.push(map[sx][y]);
        for (let x = sx; x < ex; x++) stack.push(map[x][ey]);
        for (let y = ey; y > sy; y--) stack.push(map[ex][y]);
        for (let x = ex; x > sx; x--) stack.push(map[x][sy]);
         
        const minNum = Math.min(...stack);
        result.push(minNum);
     
        const last = stack.pop();
        stack.unshift(last);
         
        for (let y = sy; y < ey; y++) map[sx][y] = stack.shift();
        for (let x = sx; x < ex; x++) map[x][ey] = stack.shift();
        for (let y = ey; y > sy; y--) map[ex][y] = stack.shift();
        for (let x = ex; x > sx; x--) map[x][sy] = stack.shift();
    }
    
    return result; 

}