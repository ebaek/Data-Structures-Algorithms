// 224: Basic Calculator

var calculate = function (s) {
    s = s.trim();
    const stack = [];

    for (let i = 0; i < s.length; i++) {
        let currChar = s.charAt(i);

        if (currChar === ")" || (stack.length >= 2 && parseInt(currChar) !== NaN) ) {
            let lastEl = stack.pop();
            let lastNum = 0;

            while (lastEl != "(" && stack.length !== 0) {

                if (lastEl !== "+" && lastEl !== "-") {
                    lastNum = lastEl;
                } else {
                    if (lastEl === "+") {
                        lastNum += parseInt(stack.pop());
                    } else {
                        lastNum -= parseInt(stack.pop());
                    }
                }
                lastEl = stack.pop();
            }
            stack.push(lastEl);
        } else if (currChar !== "(") {
            stack.push(currChar);
        }
        console.log(stack);
    }

    let lastVal = 0;
    while (stack.length) {
        let lastEl = stack.pop();
        if (lastEl === "+") {
            let num = stack.pop();
            lastVal += parseInt(num);
        } else if (lastEl === "-") {
            let num = stack.pop();
            lastVal -= parseInt(num);
        } else {
            lastVal = parseInt(lastEl);
        }
    }

    return lastVal;
};

calculate(" 2-1 + 2 ");