def largestPalindromeProduct(digits):
    palindromes = []
    n = ''
    while len(n) < digits:
        n += '9'
    n = int(n)
    for x in reversed(range(0,n+1)):
        for y in reversed(range(0,n+1)):
            f = x*y
            s = str(f)
            p1 = s[:len(s)//2]
            p2 = s[len(s)//2:]
            if p1 == p2[len(p2)::-1]:
                palindromes.append(f)
    return max(palindromes)