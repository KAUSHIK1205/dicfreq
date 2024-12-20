# Get user input for the message (tuple elements)
msg = tuple(input("Enter elements of the tuple separated by spaces: ").split())

# Get the element for which frequency is to be found
x = input("Please enter the element you want to find the frequency of: ")

# Initialize result to count frequency
result = 0

# Calculate the frequency of the element in the tuple
for k in msg:
    if k == x:
        result += 1

# Print the results
print("Tuple:", msg)
print(f"Frequency of '{x}': {result}")

# Check if specific elements are in the tuple
print("Check for ",x,":", "x" in msg)



