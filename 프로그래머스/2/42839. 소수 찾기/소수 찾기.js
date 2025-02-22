function solution(numbers) {
    const numArr = numbers.split('').map(Number);
    const primes = new Set();
    
    function getPermutation(path, used) {
        if (path.length > 0) {
            const num = Number(path.join(''));
            if (isPrime(num)) { // 소수라면 저장
                primes.add(num);
            }
        }
        
        for (let i = 0; i < numArr.length; i++) {
            if (used[i]) continue; // 사용했다면 건너뛰기
            used[i] = true;
            getPermutation([...path, numArr[i]], used);
            used[i] = false;
        }
    }
    
    getPermutation([], new Array(numArr.length).fill(false));
    return primes.size;
}

function isPrime(num) {
    if (num < 2) return false;
    
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;
}