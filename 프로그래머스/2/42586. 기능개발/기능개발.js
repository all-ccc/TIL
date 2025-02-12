function solution(progresses, speeds) {
    let days = [];
    let result = [];
    let count = 0;

    // 완료일 계산
    for (let i = 0; i < progresses.length; i++) {
        let day = Math.ceil((100 - progresses[i]) / speeds[i]);
        days.push(day);
    }

    let maxDay = days[0];
    for (let i = 0; i < days.length; i++) {
        if (days[i] <= maxDay) {
            count++;
        } else {
            result.push(count);
            count = 1;
            maxDay = days[i];
        }
    }
    
    result.push(count);

    return result;
}
