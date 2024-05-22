function solution(array, commands) {
  const result = [];
  
  for (let j = 0; j < commands.length; j++) {
    const slicedArr = array.slice(commands[j][0] - 1, commands[j][1]);
    const sortedArr = slicedArr.sort((a, b) => a - b);
    result.push(sortedArr[commands[j][2] - 1]);
  }
  
  return result;
}