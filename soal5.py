def faktorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total
n = 5
print(faktorial(n))  
