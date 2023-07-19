const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const formula = (require("fs").readFileSync(filePath).toString()).trim();

const mass = {'H':1, 'C':12, 'O':16};
const stack = [];

for (const s of formula) {
    if (s === '(') stack.push(s);
    else if (s === ')') {
        sum = 0;

        while (true) {
            target = stack.pop();
            if (target === '(') break;
            sum += target;
        }
        stack.push(sum);
    }
    else if (s in mass) stack.push(mass[s]);
    else stack[stack.length-1] *= Number(s);
}

console.log(stack.reduce((acc, cur) => acc+cur, 0))