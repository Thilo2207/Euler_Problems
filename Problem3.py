#Find the prime factors
def prime_factors():
    n = 600851475143
    factors = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    
    return factors
print("The prime factors of 600851475143 are:",prime_factors()) 
#find the largest prime factor
print("The largest prime factor is",max(prime_factors()))
