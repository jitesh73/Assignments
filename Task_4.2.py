with open('output.txt', 'wt') as fh:
    user = input('Enter text to write to the file: ')
    fh.write(str(user + '\n'))
    print("Data successfully written to output.txt.")

with open('output.txt', 'ta') as fh:
    user = input('\nEnter additional text append: ')
    fh.write(str(user))
    print("Data successfully appended.")


with open('output.txt', 'rt') as fh:
    read = fh.read()

print("\nFinal content of output.txt:")
print(read)