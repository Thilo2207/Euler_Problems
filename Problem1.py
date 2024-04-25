#Method 1
# without moduls and floor diviion
a = range(3,1000,3)
x = 0
for i in a:
    x += i
print("the sum of 3 mulitiplies is:",x)
# use floor division
c = 1000//5
y = 0
for j in range(1,c):
    d = j*5
    y += d
print("the sum of 5 mulitiples is:",y)
 
e = 1000//15
z = 0
for n in range(1,e+1):
    f = n*15
    z += f
print("the sum of 15 mulitiple is:",z)
print("the sum of 3 and 5 mulitiples is:",x + y - z) 
#Method 2 
# use moduls
total_sum = 0

for num in range(1, 1000):
    if num % 3 == 0 or num % 5 == 0:
        total_sum += num

print("The sum of these mulitiples is:", total_sum) 
