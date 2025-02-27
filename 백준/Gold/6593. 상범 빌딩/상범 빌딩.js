const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf-8').trim().split('\n'); // 제출용

let index = 0;

while (index < input.length) {
    const [L, R, C] = input[index].split(' ').map(Number);
    
    if (L === 0) break;

    index++;

    const building = [];
    let start = null;

    for (let l = 0; l < L; l++) {
        const floor = [];

        for (let r = 0; r < R; r++) {
            const row = input[index].split('');
            const sIndex = row.indexOf('S');
            if (sIndex !== -1) {
                start = [l, r, sIndex];
            }

            floor.push(row);
            index++;
        }
        building.push(floor);
        index++; // 빈 줄 건너뛰기
    }

    console.log(solution(L, R, C, building, start)); // 결과 출력

}

function solution(L, R, C, building, start) {
    const dx = [-1, 1, 0, 0, 0, 0];
    const dy = [0, 0, -1, 1, 0, 0];
    const dz = [0, 0, 0, 0, -1, 1];

    const [sx, sy, sz] = start;
    building[sx][sy][sz] = '#';
    const queue = [[sx, sy, sz, 0]];

    while (queue.length) {
        const [x, y, z, count] = queue.shift();

        for (let i = 0; i < 6; i++) {
            const nx = x + dx[i]; // 층
            const ny = y + dy[i]; // row
            const nz = z + dz[i]; // col

            if (nx >= 0 && nx < L &&
                ny >= 0 && ny < R &&
                nz >= 0 && nz < C &&
                building[nx][ny][nz] !== '#'
            ) {
                if (building[nx][ny][nz] === 'E') {
                    return `Escaped in ${count + 1} minute(s).`;
                }
                
                building[nx][ny][nz] = '#';
                queue.push([nx, ny, nz, count + 1]);
            }
        }
    }

    return 'Trapped!';
}