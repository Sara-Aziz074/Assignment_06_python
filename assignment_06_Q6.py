#You are tasked with developing a Python program to manage a student database.
#  The user should be able to add new students or stop the input process by 
# entering "stop." Each student's name, along with a sequentially generated ID 
# starting from 1, should be stored in a tuple, with these tuples kept in a list.
#  The program must check for duplicate names before adding a new student and display
#  a message if a duplicate is found. After the input process ends, the program should
#  first display the complete list of student tuples and then display each student's ID
#  and name individually. Additionally, the program should show the total number of
#  students, calculate and display the total length of all student names combined,
#  and identify the student with the longest and shortest name using appropriate operators.
#  Implement these operations within a function named manage_student_database() and
#  ensure you call this function at the end of your code.

def manage_student_database():
    # Initialize an empty list to store student records
    students = []
    # Starting ID for students
    student_id = 1

    print("Enter student names. Type 'stop' to end input.")

    while True:
        # Ask for student name
        name = input("Enter student name: ").strip()

        # Check if the user wants to stop
        if name.lower() == "stop":
            break

        # Check if the student already exists in the list by name
        if any(student[1] == name for student in students):
            print("This student is already in the database. Please enter a different name.")
            continue

        # Add the new student with a unique ID
        students.append((student_id, name))
        # Increment the ID for the next student
        student_id += 1

    # Display the full list of students
    print("\nComplete list of students:")
    for student in students:
        print(student)

    # Display each student's ID and name individually
    print("\nStudent details:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")

    # Total number of students
    total_students = len(students)
    print(f"\nTotal number of students: {total_students}")

    # Calculate the total length of all student names combined
    total_name_length = sum(len(student[1]) for student in students)
    print(f"Total length of all student names: {total_name_length}")

    # Find the student with the longest and shortest name
    if students:
        longest_name_student = max(students, key=lambda student: len(student[1]))
        shortest_name_student = min(students, key=lambda student: len(student[1]))

        print(f"Student with the longest name: {longest_name_student[1]} (ID: {longest_name_student[0]})")
        print(f"Student with the shortest name: {shortest_name_student[1]} (ID: {shortest_name_student[0]})")

# Call the function to start the program
manage_student_database()