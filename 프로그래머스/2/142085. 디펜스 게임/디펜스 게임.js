class PriorityQueue {
    constructor() {
        this.heap = [];
    }
    
    push(value) {
        this.heap.push(value);
        this._heapifyUp();
    }
    
    pop() { // 가장 작은 거 반환 및 heap에서 제거
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop();
        
        const min = this.heap[0];
        this.heap[0] = this.heap.pop(); // 맨 마지막 노드 뽑아서 맨 첫 노드 바꿔치기
        this._heapifyDown();
        return min; // 최솟값 반환
    }
    
    peek() {
        return this.heap.length === 0 ? null : this.heap[0];
    }
    
    _size() {
        return this.heap.length;
    }
    
    _heapifyUp() { // push 하고 정렬 시 사용
        let idx = this.heap.length - 1;
        while (idx > 0) {
            const parentIdx = Math.floor((idx - 1) / 2);
            if (this.heap[parentIdx] <= this.heap[idx]) break; // 잘 정렬되어있다~
            this._swap(idx, parentIdx); // 아니라면 바꿔
            idx = parentIdx; // idx 갱신
        }
    }
    
    _heapifyDown() { // pop 하고 정렬 시 사용
        let idx = 0;
        const length = this._size();
        
        while (true) {
            let smallest = idx;
            let left = idx * 2 + 1;
            let right = idx * 2 + 2;
            
            // 이제 최상위 노드로 올라간 아이의 제자리를 찾아주는 시간 ~
            if (left < length && this.heap[left] < this.heap[smallest]) {
                smallest = left; 
            }
            
            if (right < length && this.heap[right] < this.heap[smallest]) {
                smallest = right;
            }
            
            if (smallest === idx) break; // 더 이상 옮겨갈 수 없으면 종료
            
            this._swap(idx, smallest);
            idx = smallest; // 이동한 위치 기준으로 다시 검사
        }
    }
     
    _swap(i, j) {
        [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
    }
}

function solution(n, k, enemy) {
    let maxWin = 0;
    let sumEnemy = 0;
    const heap = new PriorityQueue();
    
    for (let e of enemy) {
        heap.push(-e);
        sumEnemy += e;
        
        if (sumEnemy > n) {
            if (k === 0) break;
            sumEnemy += heap.pop();
            k --;
        }
        
        maxWin++;
    }
    
    return maxWin;
}
