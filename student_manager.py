import re

FILE_NAME = "students.txt"


# Validate email using Regex
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


# Add student
def add_student():
    try:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ").strip()
        email = input("Enter Email: ").strip()

        if not name:
            raise ValueError("Name cannot be empty.")

        if not validate_email(email):
            raise ValueError("Invalid email format.")

        # Save data to file
        with open(FILE_NAME, "a") as file:
            file.write(f"{student_id},{name},{email}\n")

        print("Student added successfully!")

    except ValueError as e:
        print("Invalid Input:", e)


# Read student data
def read_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if not data:
                print("No student records found.")
                return

            print("\n--- Student Records ---")
            for line in data:
                student_id, name, email = line.strip().split(",")
                print("ID    :", student_id)
                print("Name  :", name)
                print("Email :", email)
                print("-----------------------")

    except FileNotFoundError:
        print("No student data file found.")


# Main program
def main():
    while True:
        print("\n===== Student Record Manager =====")
        print("1. Add Student")
        print("2. Read Student Data")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()

            elif choice == 2:
                read_students()

            elif choice == 3:
                print("Thank you!")
                break

            else:
                raise ValueError("Please choose 1, 2, or 3.")

        except ValueError as e:
            print("Invalid Input:", e)


main()
