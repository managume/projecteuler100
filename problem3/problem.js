function largestPrimeFactor(number){
    let largest_factor = 0
    let res = number
    for (let n = 2; n < number + 1; n++) {
        let is_divisible = true
        while (is_divisible) {
            if (res % n == 0) {
                largest_factor = n
                res = parseInt(res/n)
            }else{
                is_divisible = false
            }
        }
        if (res == 1) {
            break
        }  
    }
    return largest_factor
}

console.log(largestPrimeFactor(2))
console.log(largestPrimeFactor(3))
console.log(largestPrimeFactor(5))
console.log(largestPrimeFactor(7))
console.log(largestPrimeFactor(13195))
console.log(largestPrimeFactor(600851475143))