# Task 1: Reading a file with proper exception handling

try:
    # Try to open a file that may not exist
    with open("sample1.txt", "r") as fh:   # r = read mode
        line1 = fh.readline()
        line2 = fh.readline()

        print(f"Line 1: {line1.strip()}")
        print(f"Line 2: {line2.strip()}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
