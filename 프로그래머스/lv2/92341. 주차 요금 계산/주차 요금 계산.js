function cost(fees, time) {
    if (time <= fees[0])
        return fees[1];
    else
        return fees[1] + (Math.ceil((time - fees[0])/fees[2])*fees[3]);
}

function solution(fees, records) {
    var answer = [];
    const l = records.length;
    for (let i=0; i<l;i++) {
        [time, num, state] = records[i].split(" ");
        time = Number(time.slice(0,2))*60+Number(time.slice(3));
        records[i] = [time, num, state];
    }
    records.sort((a, b) => a[1]-b[1]);
    
    for (let i=0;i<l;i++) {
        if (records[i][2] === 'IN') {
            if (i !== l-1 && records[i][1] === records[i+1][1])
                t = records[i+1][0]-records[i][0];
            else
                t = 1439-records[i][0]; 
                
            if (i > 0 && records[i][1] === records[i-1][1])
                answer[answer.length-1] += t;
            else
                answer.push(t);
        }
    }
    return answer.map((t) => cost(fees, t));
}