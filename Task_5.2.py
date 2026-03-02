# Task 2: Demonstrate List Slicing

# Step 1: Create list from 1 to 10
numbers = list(range(1, 11))
print(f"Original list: {numbers}")

# Step 2: Extract first five elements
first_five = numbers[:5]
print(f"Extracted first five elements: {first_five}")

# Step 3: Reverse extracted elements
reversed_list = first_five[::-1]
print(f"Reversed extracted elements: {reversed_list}")      