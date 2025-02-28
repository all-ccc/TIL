function solution(w, h) {
    
    function calGcd(a, b) {
        if (a % b === 0) return b;
        return calGcd(b, a % b);
    }
    
    const gcd = calGcd(w, h);
    
    return w * h - (w + h - gcd);
}
