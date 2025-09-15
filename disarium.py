def is_disarium(num):
    digits = str(num)
    total = sum(int(digit) ** (index + 1) for index, digit in enumerate(digits))
    return total == num

number = int(input("Enter a number to check: "))
if is_disarium(number):
    print(f"{number} is a Disarium number!")
else:
    print(f"{number} is NOT a Disarium number.")

def find_disarium_in_range(start, end):
    print(f"Disarium numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_disarium(num):
            print(num, end=' ')

find_disarium_in_range(1, 200)
