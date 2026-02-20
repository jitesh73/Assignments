with open("sample.txt", 'wt') as fh:
    fh.write("This is sample text file.\n")
    fh.write("It contains multiple lines.")

try:
    with open("sample.txt", 'rt') as fh:
        Line1 = fh.readline()
        Line2 = fh.readline()

        print(f"Line 1: {Line1.strip()}")
        print(f"Line 2: {Line2}")

except FileNotFoundError:
    print(f"Error: The file 'sample1.txt' was not found.")