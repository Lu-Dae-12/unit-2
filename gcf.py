number=input("Enter a number ")
x = int(number)
factors = []

number=input("Enter a number ")
y = int(number)
factors = []

for i in range(1, min(x, y) + 1):
    if x % i == 0:
        if y % i == 0:
            factors.append(i)

print("The common factors of", number and number, "are:", factors)
