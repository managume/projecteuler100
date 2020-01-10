def multiplesOf3and5(number):
    sum=0
    for i in range(1,number):
        if (i%3) == 0:
            sum+=i
        elif (i%5) == 0:
            sum+=i
    return sum
