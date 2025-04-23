function solution(bandage, health, attacks) {
    let nowHealth = health;
    const [t, x, y] = bandage;
    let success = 0;
    let time = 0;
    
    for (let i = 0; i < attacks.length; i++) {
        let [timing, damage] = attacks[i];
        
        // 공격 전까지 회복
        for (let k = time + 1; k < timing; k++) {
            nowHealth += x;
            success++;
            
            if (success === t) {
                nowHealth += y;
                success = 0;
            }
            
            if (nowHealth > health) nowHealth = health;
        
        }
        
        nowHealth -= damage; 
        
        if (nowHealth <= 0) {
            return -1;
        }
        
        success = 0;
        time = timing;
        
    }
    
    return nowHealth;
    
}