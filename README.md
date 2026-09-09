# ⭐ Pattern Generator and Number Analyzer

A simple and interactive Python command-line application for generating star patterns and analyzing ranges of numbers.

## 📌 Project Overview

Pattern Generator and Number Analyzer is a beginner-friendly Python CLI application that combines two useful programming tasks into one interactive program.

The application allows users to:

⭐ Generate a right-angled triangular star pattern.
🔢 Analyze a range of numbers.
🟢 Identify each number as Even or Odd.
➕ Calculate the total sum of numbers in a specified range.
🔄 Perform multiple operations using an interactive menu.
🚪 Exit the application whenever the user chooses.

This project is designed to help beginners understand fundamental Python programming concepts such as loops, conditions, variables, operators, functions, and user input.

✨ Features
⭐ 1. Star Pattern Generator

Generates a right-angled triangular star pattern based on the number of rows entered by the user.

Example:

*
**
***
****
*****

🔢 2. Number Range Analyzer

Allows the user to enter a starting and ending number and analyzes every number in that range.

The program:

Checks whether each number is Even or Odd.
Displays the classification of every number.
Calculates the total sum of all numbers.
Counts the number of even and odd values.

Example:

Number 1 is Odd
Number 2 is Even
Number 3 is Odd
Number 4 is Even
Number 5 is Odd

Total Sum: 15
Even Numbers: 2
Odd Numbers: 3

📋 3. Interactive Menu

The program provides a continuous menu:

========================================
 Pattern Generator and Number Analyzer
========================================

1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit


Users can perform multiple operations without restarting the program.

🛡️ 4. Input Validation

The improved version handles invalid inputs using try-except.

For example:

Invalid input. Please enter a number.


It also checks that:

Start number <= End number


and that the number of pattern rows is positive.

🛠️ Technologies Used
Technology	Description
🐍 Python	Main programming language
💻 CLI	Command-line interface
🔤 ASCII Characters	Used for star pattern generation
📦 Dependencies

No external Python libraries are required.

The project uses only Python's built-in functionality.

📋 Requirements

Before running the project, make sure you have:

🐍 Python 3.x
💻 Terminal / Command Prompt
📝 A text editor or IDE such as VS Code, PyCharm, or IDLE
🚀 How to Run
1️⃣ Install Python

Download and install Python 3.x on your computer.

Verify the installation:

python --version


or:

python3 --version

2️⃣ Clone the Repository
git clone <your-repository-url>


Navigate to the project directory:

cd <project-folder>

3️⃣ Run the Program

Run the Python file using:

python script.py


On some systems:

python3 script.py

▶️ Example Usage
⭐ Generate a Pattern
Welcome to the Pattern Generator and Number Analyzer!

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit

Enter your choice (1/2/3): 1

Enter the number of rows for the pattern: 5

Pattern:
*
**
***
****
*****

🔢 Analyze a Number Range
Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit

Enter your choice (1/2/3): 2

Enter the start number: 1
Enter the end number: 5

Number 1 is Odd
Number 2 is Even
Number 3 is Odd
Number 4 is Even
Number 5 is Odd

Analysis Results
----------------
Range: 1 to 5
Total Sum: 15
Even Numbers: 2
Odd Numbers: 3

🚪 Exit the Program
Enter your choice (1/2/3): 3

Exiting the program... Goodbye!

🧠 Concepts Demonstrated

This project demonstrates several fundamental Python concepts.

Concept	Usage
print()	Displaying output
input()	Taking user input
int()	Converting input into integers
while loop	Maintaining the interactive menu
for loop	Iterating through rows and numbers
if-elif-else	Decision making
% operator	Checking even/odd numbers
range()	Creating number sequences
break	Exiting the program
try-except	Handling invalid input
f-strings	Formatting output
Functions	Organizing program logic
String multiplication	Creating star patterns
🔍 How Even/Odd Detection Works

The program uses the modulus operator %.

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

Example
10 % 2 = 0


Therefore, 10 is Even.

7 % 2 = 1


Therefore, 7 is Odd.

➕ How Sum Calculation Works

The program initializes the total as:

total = 0


Then every number in the range is added:

total += i


For example:

1 + 2 + 3 + 4 + 5 = 15


Therefore:

Total Sum = 15

🔄 Program Flow
                ┌─────────────┐
                │    START    │
                └──────┬──────┘
                       ↓
              ┌─────────────────┐
              │  Display Menu   │
              └────────┬────────┘
                       ↓
                ┌─────────────┐
                │ User Choice  │
                └──────┬──────┘
                       ↓
       ┌───────────────┼───────────────┐
       ↓               ↓               ↓
   Choice 1        Choice 2        Choice 3
       ↓               ↓               ↓
   Generate        Analyze          Exit
   Pattern         Numbers          Program
       ↓               ↓               ↓
       └───────────────┴───────────────┘
                       ↓
                Display Menu Again

🧮 Algorithm
⭐ Pattern Generator
1. Ask the user for the number of rows.
2. Check whether the number is positive.
3. Start a loop from 1 to the number of rows.
4. Print "*" multiplied by the current row number.
5. Display the generated pattern.

🔢 Number Analyzer
1. Ask the user for the start number.
2. Ask the user for the end number.
3. Validate the range.
4. Set total = 0.
5. Loop through every number in the range.
6. Check whether the number is even or odd.
7. Display the result.
8. Add the number to total.
9. Count even and odd numbers.
10. Display the final analysis.

📁 Suggested Project Structure
Pattern-Generator-Number-Analyzer/
│
├── 📄 script.py
├── 📄 README.md
└── 📄 LICENSE

📊 Example Test Cases
Input	Expected Result
Rows = 3	3-row star pattern
Rows = 5	5-row star pattern
Range = 1–5	Sum = 15
Range = 2–6	Sum = 20
Range = 10–15	Even/Odd classification
Choice = 3	Program exits
Choice = 5	Invalid choice message
⚠️ Error Handling

The program handles common input errors.

❌ Invalid Number
Enter the number of rows: abc

Invalid input. Please enter a number.

❌ Invalid Range
Enter the start number: 10
Enter the end number: 5

Start number must be less than or equal to end number.

❌ Invalid Menu Choice
Enter your choice (1/2/3): 7

Invalid choice. Please select 1, 2, or 3.

📈 Future Enhancements

The project can be expanded with additional features such as:

🔺 Pyramid and inverted pyramid patterns.
🔢 Prime number detection.
🧮 Factorial calculation.
🌀 Fibonacci series