function solution(n, works) {
    works.sort((a, b) => b - a);

    while (n > 0) {
        if (works[0] === 0) break;
        
        const max = works[0];
        
        for (let i = 0; i < works.length; i++) {
            if (works[i] >= max) {
                works[i]--;
                n--;
            }
            if (!n) break;
        }
    }
    
    return works.reduce((acc, cur) => acc + cur ** 2, 0);
}