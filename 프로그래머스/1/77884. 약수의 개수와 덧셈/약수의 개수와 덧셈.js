function solution(left, right) {
    let sum = 0;
    for(let i = left; i <= right; i++){
        sum = sum + count(i) * i
    }
    return sum;
}

function count(num){
    let count = 0;
    for(let i = 1; i <= num; i++){
        if(num % i === 0){
            count = count + 1
        }
    }
    return count % 2 === 1 ? -1 : 1
}