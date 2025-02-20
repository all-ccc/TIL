function solution(book_time) {
    book_time.sort((a, b) => changeMin(a[0]) - changeMin(b[0]));

    const rooms = []; // 사용하고 있는 방의 끝나는 시간 저장

    for (let time of book_time) {
        const start = changeMin(time[0]);
        const end = changeMin(time[1]) + 10;

        for (let i = 0; i < rooms.length; i++) {
            if (rooms[i] <= start) { // 안 겹치면
                rooms.splice(i, 1);
                break;
            }
        }

        rooms.push(end);
    }

    return rooms.length;
}

function changeMin(time) {
    const [hour, min] = time.split(':').map(Number);
    return hour * 60 + min;
}