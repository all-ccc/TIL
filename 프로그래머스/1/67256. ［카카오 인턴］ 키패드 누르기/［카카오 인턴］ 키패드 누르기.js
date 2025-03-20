function solution(numbers, hand) {
    let result = '';
    hand = hand === 'right' ? 'R' : 'L';
    let cur = [[3, 0], [3, 2]];
    
    for (let number of numbers) {
        let coordinate = getCoor(number);
        
        if ([1, 4, 7].includes(number)) {
            result += 'L'
            cur[0] = coordinate;
        } else if ([3, 6, 9].includes(number)) {
            result += 'R'
            cur[1] = coordinate;
        } else {
            let closeHand = getCloser(coordinate);
            result += closeHand;
        }
    }
    
    // 좌우 중 어디랑 가까운지 구하는 함수
    function getCloser(target) {
        let leftDis = Math.abs(cur[0][0] - target[0]) + Math.abs(cur[0][1] - target[1]);
        let rightDis = Math.abs(cur[1][0] - target[0]) + Math.abs(cur[1][1] - target[1]);
        
        if (leftDis < rightDis) {
            cur[0] = target;
            return 'L';
        } else if (leftDis > rightDis) {
            cur[1] = target;
            return 'R';
        } else {
            if (hand === 'L') {
                cur[0] = target;
            } else {
                cur[1] = target;
            }
            
            return hand;
        }
    }
    
    // 번호 -> 좌표로 바꾸는 함수
    function getCoor(num) {
        if (num === 0) {
            return [3, 1];
        }

        return [Math.floor((num - 1) / 3), (num - 1) % 3];
    }
    
    return result;
}

