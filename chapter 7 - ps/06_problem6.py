n = int(input("Enter your no.: "))

factor = 1
i = 1

while(i<=n):
    factor *= i
    i += 1

print(factor)

n = int(input("Enter your no.: "))
product = 1
for i in range(1, n+1):
    product = product * i 
print(f"The factorial of {n} is {product}")