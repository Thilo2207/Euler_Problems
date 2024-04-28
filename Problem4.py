#Find Largest Palindrome Product
def isstring(n):
    return str(n) == str(n)[::-1]
Largest_Palindrome = 0
for i in range(100,1000):
    for j in range(100,1000):
        product = i*j
        if isstring(product) and product > Largest_Palindrome:
            Largest_Palindrome = product
            
print("the largest palindrome made from the product of two 3-digit numbers:",Largest_Palindrome)

    