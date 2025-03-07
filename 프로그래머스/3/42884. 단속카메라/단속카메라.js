function solution(routes) {
    let result = 1; 
    routes.sort((a, b) => a[1] - b[1]);
    let lastCam = routes[0][1];
    
    for (let i = 1; i < routes.length; i++) {
        if (routes[i][0] > lastCam) {
            result++;
            lastCam = routes[i][1];
        }
    }
    
    return result;
    
}