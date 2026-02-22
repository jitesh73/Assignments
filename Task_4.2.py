# Task 2: Writing, Appending and Reading a File

# w = write mode (creates file or overwrites)
with open('output.txt', 'w') as fh:
    user = input('Enter text to write to the file: ')
    fh.write(user + '\n')
    print("Data successfully written to output.txt.")

# a = append mode (adds data to existing file)
with open('output.txt', 'a') as fh:
    user = input('\nEnter additional text to append: ')
    fh.write(user + '\n')
    print("Data successfully appended.")

# r = read mode
with open('output.txt', 'r') as fh:
    read = fh.read()

print("\nFinal content of output.txt:")
print(read)