function solution(targets) {
    var answer = [];
    targets.sort((a,b) => a[0]-b[0]);
    
    let s,e;
    answer.push(targets[0]);
    targets.slice(1).map((target) => {
        [s,e] = target;
        if (answer[answer.length-1][0] >= e || answer[answer.length-1][1] <= s) {
            answer.push(target);
        } else {
            answer[answer.length-1][0] = s
            answer[answer.length-1][1] = Math.min(answer[answer.length-1][1],e);
        }   
    });
    return answer.length;
}