inputnumbers = [int(num) for num in input("Please give some numbers: ").split()]

smallest, second = inputnumbers[0], inputnumbers[1]

for num in inputnumbers[2:]:
    if num < smallest:
        second = smallest
        smallest = num
    elif num < second:
        second = num

print(second)
