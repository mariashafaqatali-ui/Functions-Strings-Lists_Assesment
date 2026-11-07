"""Task 1: Student Result Card Generator
Topics: Functions (def, parameters, return) and String Manipulation
"""

SUBJECTS = ["English", "Urdu", "Mathematics", "Science", "Computer"]
MAX_MARKS_PER_SUBJECT = 100
SUBJECT_PASS_MARK = 40


def format_name(name):
    """Remove extra spaces and capitalise each word of the name."""
    return name.strip().title()


def get_valid_marks(subject):
    """Keep asking until the user enters marks between 0 and 100."""
    while True:
        value = input(f"Enter marks in {subject} (0-100): ").strip()
        try:
            marks = int(value)
        except ValueError:
            print("  Invalid input. Please enter a whole number.")
            continue

        if 0 <= marks <= 100:
            return marks
        print("  Marks must be between 0 and 100.")


def calculate_percentage(total, max_total):
    """Return the percentage obtained."""
    return (total / max_total) * 100


def get_grade(percentage):
    """Return the letter grade for a given percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


def get_valid_roll_number():
    """Keep asking until the roll number contains digits only."""
    while True:
        roll_no = input("Enter roll number: ").strip()
        if roll_no.isdigit():
            return roll_no
        print("  Roll number must contain digits only.")


def get_valid_name():
    """Keep asking until a non-empty name is entered, then clean it."""
    while True:
        name = input("Enter student name: ")
        if name.strip():
            return format_name(name)
        print("  Name cannot be empty.")


def print_result_card(name, roll_no, marks_list, total, max_total, percentage, grade, status):
    """Display the formatted result card using f-strings."""
    line = "=" * 40
    print()
    print(line)
    print(f"{'STUDENT RESULT CARD':^40}")
    print(line)
    print(f"Name        : {name}")
    print(f"Roll Number : {roll_no}")
    print("-" * 40)
    print(f"{'Subject':<20}{'Marks':>10}{'Out of':>10}")
    print("-" * 40)
    for subject, marks in marks_list:
        print(f"{subject:<20}{marks:>10}{MAX_MARKS_PER_SUBJECT:>10}")
    print("-" * 40)
    print(f"{'Total Marks':<20}{total:>10}{max_total:>10}")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Grade       : {grade}")
    print(f"Status      : {status}")
    print(line)


def main():
    print("=== Student Result Card Generator ===\n")

    name = get_valid_name()
    roll_no = get_valid_roll_number()

    marks_list = []
    for subject in SUBJECTS:
        marks = get_valid_marks(subject)
        marks_list.append((subject, marks))

    total = sum(marks for _, marks in marks_list)
    max_total = len(SUBJECTS) * MAX_MARKS_PER_SUBJECT
    percentage = calculate_percentage(total, max_total)
    grade = get_grade(percentage)

    # If any subject is below 40, the final result is Fail regardless of percentage
    failed_subject = any(marks < SUBJECT_PASS_MARK for _, marks in marks_list)
    if failed_subject:
        grade = "Fail"

    status = "Fail" if grade == "Fail" else "Pass"

    print_result_card(name, roll_no, marks_list, total, max_total, percentage, grade, status)

    if failed_subject:
        print(f"Note: Marks below {SUBJECT_PASS_MARK} in a subject mean the final result is Fail.")


if __name__ == "__main__":
    main()