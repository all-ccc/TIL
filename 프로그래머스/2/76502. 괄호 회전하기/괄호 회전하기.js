function solution(s) {
    let arr = [...s];
    let result = 0;
    let len = s.length;
    for (let i = 0; i < len; i++) {
        let newArr = s.slice(i).concat(s.slice(0, i));
        
        if (checkStr(newArr)) {
            result++;
        }
    }
    
    return result;


    function checkStr(brackets) {
        const stack = [];
        const bracketSet = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        
        for (let b of brackets) {
            if (b === '(' || b === '{' || b === '[') { // 열린 괄호
                stack.push(b);
            } else { // 닫힌 괄호
                if (stack.length === 0) return false;

                let open = stack.pop();
                if (b !== bracketSet[open]) return false;
            }
        }
        
        if (stack.length === 0) return true;
    }
}