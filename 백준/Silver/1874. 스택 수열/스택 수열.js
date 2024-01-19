const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function solve(input) {
  const lines = input.trim().split("\n");
  const n = parseInt(lines[0]);

  const stack = [];
  let top = 0;
  let index = 1;
  let result = "";

  while (index <= n) {
    const value = parseInt(lines[index]);

    if (value > top) {
      for (let i = top; i < value; i++) {
        stack.push(i + 1);
        result += "+\n";
      }
      top = value;
    } else if (stack[stack.length - 1] !== value) {
      console.log("NO");
      return;
    }

    stack.pop();
    result += "-\n";
    index++;
  }

  console.log(result);
}

let input = "";

rl.on("line", (line) => {
  input += line + "\n";
});

rl.on("close", () => {
  solve(input);
});
