# Find the Fibonacci sequence 
a, b = 1, 2
sequence = [a, b]
while True:
    next_number = a + b
    if next_number > 4000000:
        break
    sequence.append(next_number)
    a, b = b, next_number
#find the sum of the even-valued terms.
Even_Value_Sum = 0
for x in sequence:
    if x % 2 == 0:
        Even_Value_Sum += x
print(Even_Value_Sum)