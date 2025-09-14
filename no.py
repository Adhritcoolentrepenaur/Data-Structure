# Dictionary with number meanings
meanings =
1:"Good" # type: ignore

# Ask the user for a number
num = int(input("Enter a number: "))

# Show the meaning
print("Meaning:", meanings.get(num, "Not found"))



1