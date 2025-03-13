function solution(a, b, c, d) {
    const nums = [a, b, c, d].sort();
    const setNums = [...new Set(nums)];
    
    if (setNums.length === 1) { // 네 개가 모두 같은 경우
        return a * 1111; 
    } 
    
    if (setNums.length === 4) { // 네 개가 모두 다른 경우
        return nums[0];
    } 
    
    if (setNums.length === 2) { // (3개 + 1개) or (2개 + 2개)
        const [p, q] = setNums;
        const countP = nums.filter(v => v === p).length;

        if (countP === 3) { // 셋 하나
            return (10 * p + q) ** 2;
        } else if (countP === 1) { // 하나 셋
            return (10 * q + p) ** 2;
        } else { // 둘 둘
            return (p + q) * Math.abs(p - q); 
        }
    } 
    
    if (setNums.length === 3) { // (2개 + 1개 + 1개)
        let q, r;
        // 반복문을 돌면서 두 번 나온 숫자 제거
        for (let i = 0; i < 3; i++) {
            if (nums.filter(v => v === setNums[i]).length === 2) {
                setNums.splice(i, 1);
                break;
            }
        }
        
        [q, r] = setNums;
        
        return q * r; 
    }
}
