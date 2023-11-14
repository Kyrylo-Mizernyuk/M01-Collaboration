# Kyrylo Mizernyuk
# 2023-11-06
# honor_roll_checker.py
#
# This Python script takes student names and GPAs as input,
# then checks and prints if the student qualifies for the Dean's List
# (GPA of 3.5 or greater) or the Honor Roll (GPA of 3.25 or greater).
# The processing stops when 'ZZZ' is entered as a last name.

def check_qualifications(first_name, last_name, gpa):
    """Check and print the student's qualification status."""
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} has not qualified for the Dean's List or Honor Roll.")

def get_student_info():
    """Collect student information and check qualifications."""
    while True:
        last_name = input("Please enter the student's last name (enter 'ZZZ' to quit): ")
        if last_name == 'ZZZ':
            break

        first_name = input("Please enter the student's first name: ")
        gpa = float(input("Please enter the student's GPA: "))

        check_qualifications(first_name, last_name, gpa)

# Main execution
if __name__ == "__main__":
    print("Honor Roll and Dean's List Qualification Checker\n")
    get_student_info()
