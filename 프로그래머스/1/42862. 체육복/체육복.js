function solution(n, lost, reserve) {
    const total = new Array(n + 1).fill(1);
    
    for (let i of reserve) total[i] += 1; // 여벌 체육복 있는 학생
    for (let i of lost) total[i] -= 1; // 체육복 도난당한 학생
    
    for (let i = 1; i <= n; i++) {
        if (total[i] === 0) {
            if (i > 1 && total[i-1] === 2) { // 앞번호 학생이 여벌이 있을 때
                total[i] += 1;
                total[i-1] -= 1;
            } else if (total[i+1] === 2) { // 뒷번호 학생이 여벌이 있을 때
                total[i] += 1;
                total[i+1] -= 1;
            }
        }
    }
    return total.filter((value) => value >= 1).length - 1;
}