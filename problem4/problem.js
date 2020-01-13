function largestPalindromeProduct(digits) {
    let palindromes = []
    let n = ''
    while (n.length < digits) {
        n += '9'
    }
    for (let x = parseInt(n); x > 0; x--) {
        for (let y = parseInt(n); y > 0; y--) {
            let f = x*y
            let s = f.toString()
            let p1 = s.substring(0, s.length/2)
            let p2 = s.substring(s.length/2, s.length).split("").reverse().join("")
            if (p1 == p2) {
                palindromes.push(parseInt(f))
            } 
        }
    }
    return Math.max.apply(null,palindromes)
}

console.log(largestPalindromeProduct(2))
console.log(largestPalindromeProduct(3))