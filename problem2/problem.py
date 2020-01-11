def fiboEvenSum(n):
    fibonacci = []
    for i,j in enumerate(range(0,n+2)):
        if j == 0:
            fibonacci.append(0)
        elif j == 1:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
    return sum([x for x in fibonacci if x%2==0])