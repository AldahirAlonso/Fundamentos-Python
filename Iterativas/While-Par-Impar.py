oddNumbers = 0
evenNumbers = 0
number = int(input("Enter a number or type 0 to stop: "))
while number != 0:
    if number % 2 == 1:
        oddNumbers += 1
    else:
        evenNumbers += 1
    number = int(input("Enter a number or type 0 to stop: "))
print("Odd numbers count:", oddNumbers)
print("Even numbers count:", evenNumbers)