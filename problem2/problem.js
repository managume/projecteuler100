function fiboEvenSum(n){
    let fibonacci = []
    let sum = 0
    for (let index = 0; index < n+2; index++) {
        if(index == 0){
            fibonacci.push(0)
        }else if(index == 1){
            fibonacci.push(1)
        }else{
            fibonacci.push(fibonacci[index-2] + fibonacci[index-1])
        }
    }
    fibonacci.forEach(element => {
        if (element%2 == 0){
            sum = sum + element
        }
    });
    return sum;
}

console.log(fiboEvenSum(10))
console.log(fiboEvenSum(18))
console.log(fiboEvenSum(23))
console.log(fiboEvenSum(43))