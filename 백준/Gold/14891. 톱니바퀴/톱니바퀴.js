const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(line => line.trim());

const wheels = [[]];
const T = Number(input[4]);

for (let i = 0; i < 4; i++) {
    const status = input[i].split('').map(Number);
    wheels.push(status);
}

function rotate(wheel, dir) {
    if (dir === 1) { // 시계 방향
        wheel.unshift(wheel.pop());
    } else if (dir === -1) {
        wheel.push(wheel.shift());
    }
}

for (let t = 5; t < 5 + T; t++) {
    const [num, dir] = input[t].split(' ').map(Number);
    const rotateDir = Array(5).fill(0);
    rotateDir[num] = dir;

    // 왼쪽
    for (let i = num - 1; i >= 1; i--) {
        if (wheels[i][2] !== wheels[i + 1][6]) {
            rotateDir[i] = -rotateDir[i + 1];
        } else {
            break;
        }
    }

    // 오른쪽
    for (let i = num + 1; i <= 4; i++) {
        if (wheels[i - 1][2] !== wheels[i][6]) {
            rotateDir[i] = -rotateDir[i - 1];
        } else {
            break;
        }
    }

    for (let i = 1; i <= 4; i++) {
        if (rotateDir[i] !== 0) {
            rotate(wheels[i], rotateDir[i]);
        }
    }
}

let a = wheels[1][0] ? 1 : 0;
let b = wheels[2][0] ? 2 : 0;
let c = wheels[3][0] ? 4 : 0;
let d = wheels[4][0] ? 8 : 0;

console.log(a + b + c + d);

