"""Task 2: Class Marks Analyzer
Topics: Lists (append, len, sum, max, min, sorted) and Loops
"""

PASS_MARK = 50  # marks needed to pass


def get_valid_student_count():
    # Ask for the number of students until a positive whole number is entered
    while True:
        value = input("How many students are in the class? ").strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("  Please enter a whole number greater than 0.")


def get_valid_name(position):
    # Ask for a student's name and reject empty input
    while True:
        name = input(f"Enter name of student {position}: ").strip().title()
        if name:
            return name
        print("  Name cannot be empty.")


def get_valid_marks(name):
    # Ask for marks until the value is a whole number between 0 and 100
    while True:
        value = input(f"  Enter marks for {name} (0-100): ").strip()
        try:
            marks = int(value)
        except ValueError:
            print("  Invalid input. Marks must be a whole number.")
            continue

        if 0 <= marks <= 100:
            return marks
        print("  Marks must be between 0 and 100.")


def find_students_with_marks(student_names, student_marks, target_marks):
    # Return the names of all students who scored exactly target_marks
    matching_names = []
    for index in range(len(student_marks)):
        if student_marks[index] == target_marks:
            matching_names.append(student_names[index])
    return matching_names


def count_pass_and_fail(student_marks):
    # Count how many students passed (>= PASS_MARK) and how many failed
    passed = 0
    failed = 0
    for marks in student_marks:
        if marks >= PASS_MARK:
            passed += 1
        else:
            failed += 1
    return passed, failed


def show_above_average(student_names, student_marks, average):
    # Print every student who scored strictly above the class average
    print(f"\nStudents above class average ({average:.2f}):")
    found = False
    for index in range(len(student_marks)):
        if student_marks[index] > average:
            print(f"  - {student_names[index]}: {student_marks[index]}")
            found = True
    if not found:
        print("  No student scored above the class average.")


def show_sorted_marks(student_names, student_marks):
    # Print students from highest to lowest marks (original order kept for ties)
    paired = list(zip(student_names, student_marks))
    ranked = sorted(paired, key=lambda pair: pair[1], reverse=True)

    print("\nMarks sorted from highest to lowest:")
    for position, (name, marks) in enumerate(ranked, start=1):
        print(f"  {position}. {name:<15} {marks:>3}")


def main():
    print("=== Class Marks Analyzer ===\n")

    student_names = []
    student_marks = []

    total_students = get_valid_student_count()

    # Collect names and marks, storing each in its own list
    for position in range(1, total_students + 1):
        name = get_valid_name(position)
        marks = get_valid_marks(name)
        student_names.append(name)
        student_marks.append(marks)
        print()

    # Basic statistics
    class_average = sum(student_marks) / len(student_marks)
    highest = max(student_marks)
    lowest = min(student_marks)

    print("=" * 40)
    print(f"{'CLASS ANALYSIS':^40}")
    print("=" * 40)
    print(f"Total students : {len(student_names)}")
    print(f"Class average  : {class_average:.2f}")

    top_students = find_students_with_marks(student_names, student_marks, highest)
    print(f"Highest marks  : {highest} ({', '.join(top_students)})")

    low_students = find_students_with_marks(student_names, student_marks, lowest)
    print(f"Lowest marks   : {lowest} ({', '.join(low_students)})")

    passed, failed = count_pass_and_fail(student_marks)
    print(f"Passing (>= {PASS_MARK}): {passed}")
    print(f"Failing (< {PASS_MARK}) : {failed}")

    show_above_average(student_names, student_marks, class_average)
    show_sorted_marks(student_names, student_marks)
    print("=" * 40)


if __name__ == "__main__":
    main()