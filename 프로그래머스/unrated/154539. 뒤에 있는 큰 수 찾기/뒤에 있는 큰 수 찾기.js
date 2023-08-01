function solution(numbers) {
    var answer = Array(numbers.length).fill(-1);
    var stack = [];
    numbers.forEach((num, i) => {
        while (stack.length && numbers[stack[stack.length-1]] < num)
            answer[stack.pop()] = num;
        stack.push(i);
    })
    return answer;
}