def largestPrimeFactor(number):
    largest_factor = 0
    res = number
    for n in range(2,number+1):
        is_divisible = True
        while is_divisible:
            if res % n == 0:
                largest_factor = n
                res = int(res/n)
            else:
                is_divisible=False
        if res == 1:
            break
    return largest_factor