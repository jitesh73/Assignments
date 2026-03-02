# Task 1: Create a Dictionary of Student Marks

# Step 1: Create dictionary
student_details = {
    "Alice" : 89,
    "Bob" : 75,
    "Charlie" : 80,
    "David" : 95,
    "Eve" : 69,
}

# Step 2: Ask user for student name
s_name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks
if s_name in student_details:
    print(f"{s_name}'s marks: {student_details[s_name]}")
else:
    print("Student not found.")