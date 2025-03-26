function solution(skill, skill_trees) {
    let result = 0;
    
    for (let tree of skill_trees) {
        let idx = 0;
        let possible = true;
        
        for (let i = 0; i < tree.length; i++) {
            let now = tree[i];
            if (!skill.includes(now)) continue;

            if (skill[idx] === now) {
                idx++;
            } else {
                possible = false;
                break;
            }
        }
        
        if (possible) result++;
    }    

    return result;
}