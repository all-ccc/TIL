function solution(rank, attendance) {
    let ranks = [];

    for (let i = 0; i < rank.length; i++) {
        if (attendance[i]) {  // 가능한 애들만 넣음
            ranks.push({ rank: rank[i], index: i });
        }
    }

    ranks.sort((a, b) => a.rank - b.rank);

    let [a, b, c] = ranks;

    return 10000 * a.index + 100 * b.index + c.index;
}
