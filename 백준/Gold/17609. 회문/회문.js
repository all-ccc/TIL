const fs = require('fs');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n').map(line => line.trim()); // 줄 끝의 공백 및 \r 제거
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n'); // 제출용
 
const T = Number(input[0]);

function isPalindrome(str, left, right, isUsed) {
    while (left < right) {
        if (str[left] === str[right]) {
            left++;
            right--;
        } else {
            if (isUsed) return 2;
            const leftMove = isPalindrome(str, left + 1, right, true);
            const rightMove = isPalindrome(str, left, right - 1, true);
            return Math.min(leftMove, rightMove); 
        }
    }

    return isUsed ? 1 : 0;
}

for (let i = 1; i <= T; i++) { 
    const word = input[i];
    const len = word.length;
    console.log(isPalindrome(word, 0, len - 1, false));
}