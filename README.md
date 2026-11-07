<div align="center">

# 🐍 Python Practice Tasks

### Result Card Generator &nbsp;•&nbsp; Class Marks Analyzer

Two beginner-friendly command-line Python programs that practise **functions**, **string manipulation**, **lists** and **loops**.

<img src="https://img.shields.io/badge/Python-3.6%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.6+">
<img src="https://img.shields.io/badge/Interface-Command_Line-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="Command line interface">
<img src="https://img.shields.io/badge/Dependencies-None-2ea44f?style=for-the-badge" alt="No dependencies">
<img src="https://img.shields.io/badge/Programs-2-8b5cf6?style=for-the-badge" alt="2 programs">

</div>

---

## 📌 Projects

| # | Program | File | Topics |
|---|---|---|---|
| 1 | 🎓 Student Result Card Generator | `result_card_generator.py` | Functions (`def`, parameters, `return`), string manipulation |
| 2 | 📊 Class Marks Analyzer | `class_marks_analyzer.py` | Lists (`append()`, `len()`, `sum()`, `max()`, `min()`, `sorted()`), loops |

## 🧰 Built With

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)

## ⚙️ Requirements

- Python 3.6 or higher (the programs use f-strings)
- No third-party packages

## ▶️ How to Run

```bash
python result_card_generator.py
python class_marks_analyzer.py
```

On some systems the command is `python3` instead of `python`.

---

## 🎓 Task 1: Student Result Card Generator

![Functions](https://img.shields.io/badge/Functions-3776AB?style=flat-square)
![Strings](https://img.shields.io/badge/String_Manipulation-8b5cf6?style=flat-square)
![Validation](https://img.shields.io/badge/Input_Validation-14b8a6?style=flat-square)

Generates a formatted result card for one student.

### ✨ What it does

- Asks for the student's name, roll number and marks in five subjects (English, Urdu, Mathematics, Science, Computer)
- Cleans the name with `.strip()` and `.title()`
- Checks the roll number with `.isdigit()`
- Accepts marks only between 0 and 100 and asks again on invalid input
- Calculates the total and the percentage (shown to 2 decimal places)
- Assigns a grade and a final Pass/Fail status
- Prints the result card using f-strings

### 🏅 Grading criteria

| Percentage | Grade |
|---|---|
| 90 and above | 🥇 A+ |
| 80 to 89 | 🥈 A |
| 70 to 79 | 🥉 B |
| 60 to 69 | C |
| 50 to 59 | D |
| Below 50 | ❌ Fail |

> ⚠️ **Important rule:** if any subject has marks below 40, the final result is **Fail**, regardless of the overall percentage.

### 🧩 Functions

| Function | Purpose |
|---|---|
| `format_name(name)` | Removes extra spaces and capitalises each word |
| `get_valid_marks(subject)` | Keeps asking until marks are between 0 and 100 |
| `calculate_percentage(total, max_total)` | Returns the percentage obtained |
| `get_grade(percentage)` | Returns the letter grade for a percentage |
| `get_valid_roll_number()` | Keeps asking until the roll number has digits only |
| `get_valid_name()` | Keeps asking until a non-empty name is entered |
| `print_result_card(...)` | Displays the formatted result card |
| `main()` | Runs the program |

### 🖥️ Sample output

```
========================================
          STUDENT RESULT CARD           
========================================
Name        : Maria Ali
Roll Number : 123
----------------------------------------
Subject                  Marks    Out of
----------------------------------------
English                     95       100
Urdu                        88       100
Mathematics                 92       100
Science                     85       100
Computer                    79       100
----------------------------------------
Total Marks                439       500
Percentage  : 87.80%
Grade       : A
Status      : Pass
========================================
```

**Below-40 rule example:** a student with 100 marks in four subjects and 35 in the fifth gets 87.00%, but the result is still shown as `Grade: Fail` and `Status: Fail`.

---

## 📊 Task 2: Class Marks Analyzer

![Lists](https://img.shields.io/badge/Lists-3776AB?style=flat-square)
![Loops](https://img.shields.io/badge/Loops-8b5cf6?style=flat-square)
![Sorting](https://img.shields.io/badge/Sorting-14b8a6?style=flat-square)

Analyzes the academic performance of a whole class.

### ✨ What it does

- Asks how many students are in the class
- Stores names and marks in two separate lists, `student_names` and `student_marks`, using `.append()`
- Validates every mark (0 to 100) and asks again if the input is invalid
- Calculates and displays:
  - 📈 Class average
  - 🏆 Highest marks and the student(s) who achieved them
  - 📉 Lowest marks and the student(s) who achieved them
  - ✅ Number of passing students (50 or above) and ❌ failing students (below 50)
  - ⭐ Students who scored above the class average
  - 🔢 All students sorted from highest to lowest marks

### 🧩 Functions

| Function | Purpose |
|---|---|
| `get_valid_student_count()` | Asks for a positive whole number of students |
| `get_valid_name(position)` | Asks for a student's name and rejects empty input |
| `get_valid_marks(name)` | Asks for marks until they are between 0 and 100 |
| `find_students_with_marks(...)` | Returns every student who scored exactly the given marks |
| `count_pass_and_fail(student_marks)` | Counts passing and failing students |
| `show_above_average(...)` | Prints students scoring above the class average |
| `show_sorted_marks(...)` | Prints students from highest to lowest marks |
| `main()` | Runs the program |

### 🖥️ Sample output

```
========================================
             CLASS ANALYSIS             
========================================
Total students : 4
Class average  : 74.25
Highest marks  : 90 (Ali, Bilal)
Lowest marks   : 45 (Sara)
Passing (>= 50): 3
Failing (< 50) : 1

Students above class average (74.25):
  - Ali: 90
  - Bilal: 90

Marks sorted from highest to lowest:
  1. Ali              90
  2. Bilal            90
  3. Hina             72
  4. Sara             45
========================================
```

---

## 🛡️ Input Validation

| Input | Rule | What happens on invalid input |
|---|---|---|
| Marks | Whole number from 0 to 100 | ✅ Shows an error and asks again |
| Roll number (Task 1) | Digits only | ✅ Shows an error and asks again |
| Student name | Not empty | ✅ Shows an error and asks again |
| Number of students (Task 2) | Whole number greater than 0 | ✅ Shows an error and asks again |

## 🧪 Testing

Both programs were tested with several scenarios.

**Task 1**
- ✅ Name with extra spaces and lowercase letters (cleaned to title case)
- ✅ Invalid roll number (`abc`) followed by a valid one
- ✅ Invalid marks (`150`, `xyz`) followed by valid marks
- ✅ High overall percentage with one subject below 40 (result is Fail)

**Task 2**
- ✅ Two students tied for the highest marks (both names shown)
- ✅ Invalid input (0 students, `abc`, empty name, marks `150`, `-5`, `xyz`) followed by valid input
- ✅ All students with the same marks (no one above average)
- ✅ A class with a single student
- ✅ Boundary check: 50 marks passes and 49 marks fails

## 📁 Project Structure

```
.
├── README.md
├── result_card_generator.py
└── class_marks_analyzer.py
```

<div align="center">

Made with 🐍 Python

</div>
