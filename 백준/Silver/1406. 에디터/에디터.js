const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(line => line.trim());

const str = input[0];
const T = Number(input[1]);
const left = [...str];
const right = [];

for (let i = 2; i < T + 2; i++) {
    let cmd = input[i];

    if (cmd === 'L') {
        if (left.length > 0) {
            right.push(left.pop());
        }
    } else if (cmd === 'D') {
        if (right.length > 0) {
            left.push(right.pop());
        }
    } else if (cmd === 'B') {
        if (left.length > 0) {
            left.pop();
        }
    } else {
        left.push(cmd[2]);
    }
}

console.log(left.concat(right.reverse()).join(''));