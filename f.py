number=input("Enter a number")
num = int(number)
factors = []

for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)
        