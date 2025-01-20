# As_1

print("Ishan")
print("Ishan")
print("Ishan")

# As_2
a=1
b=1
c=1
print(a+b+c)
a="he"
b="is"
c="kind"
d=a+b+c
print(d)

# As_4
for i in range(1,11):
    print("7 x ",i,"= ",7*i)
for i in range(1,11):
    print("9 x ",i,"= ",9*i)
n3=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
n1=int(input("Enter a number:"))
for i in range(1,11):
    print(n," x ",i,"= ",n*i)
s=0
for i in range(1,n+1):
    s=s+i
for i in range(2,n3+1):
    f=0
    for j in range(2,i//2 +1):
        if (i%j==0):
            f=1
            break
    if f==0:
        print(i)
    
# As_5
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

maximum = max(num1, num2, num3)

print(f"The maximum among {num1}, {num2}, and {num3} is: {maximum}")

n = int(input("Enter the value of n: "))

total_sum = 0

for i in range(1, n + 1):
    if i % 7 == 0 and i % 9 == 0:
        total_sum += i

print(f"The sum of all numbers divisible by 7 and 9 from 1 to {n} is: {total_sum}")

n = int(input("Enter the value of n: "))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_sum = 0

for i in range(1, n + 1):
    if is_prime(i):
        prime_sum += i

print(f"The sum of all prime numbers from 1 to {n} is: {prime_sum}")





# As_6
n=int(input("Enter a Number:"))

def SumOdd(n):
    s=0;
    for i in range(1,n+1):
        if (i%2 !=0):
            s=s+i
    print(s)

SumOdd(n)

def PrimeSum(n):
    s=0
    for i in range(2,n+1):
        f=0
        for j in range(2,i//2+1):
            if (i%j==0):
                f=1
                break
        if f==0:
            s=s+i
    print(s)

PrimeSum(n)

