# Python Programming Assessment – Strings & Data Processing

## Candidate Information

**Name:** Saurabh Ravindra Bhonsle

**Role:** Python Developer Intern Assessment

**Company:** Embed Square Solutions Pvt. Ltd.

**Submission Date:** 26 August 2026

---

## Overview

This repository contains my solutions for the **Python Programming Assessment – Strings & Data Processing** conducted by Embed Square Solutions.

The assessment evaluates fundamental Python programming concepts related to string manipulation, iteration, character handling, conditional logic, and writing clean, structured functions.

---

## Problem Statement

The assessment consists of the following tasks:

1. Reverse a String
2. Count Vowels in a String

The solutions are implemented using multiple programming approaches for better understanding and comparison.

---

## Solutions Included

### Question 1 – Reverse String

The repository includes three implementations of the Reverse String problem:

| Approach | Input Type | Time Complexity |
|----------|------------|-----------------|
| Object-Oriented Programming (Class & Object) | User Input | O(n²) |
| Function-Based (Two Pointer Technique) | User Input | O(n) |
| Object-Oriented Programming (Class & Object) | Hardcoded Input | O(n²) |

Each implementation follows a modular structure using a separate `main()` function.

---

## Approach

### Reverse String using OOP

- Created a `StringOperations` class.
- Implemented a `reverse_string()` method.
- Created an object inside `main()` and invoked the method.
- Displayed the original and reversed strings.

### Reverse String using Two Pointer Technique

- Converted the string into a list of characters.
- Used two pointers (`start` and `end`) to swap characters.
- Joined the list back into a string and returned the result.

---

## Edge Cases Handled

The implementations handle the following scenarios:

- Empty string input.
- Single-character string.
- Strings containing spaces.
- Uppercase and lowercase characters.
- Numeric characters.
- Special characters.

---

## Project Structure

```text
es-python-assessment-strings-data-processing-saurabh-bhonsle/
│
├── reverse_string.py
└── README.md
```

---

## Python Version

**Recommended Version:** Python 3.10 or above

Check your installed version:

```bash
python --version
```

or

```bash
python3 --version
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-link>
```

### 2. Open the Project Directory

```bash
cd es-python-assessment-strings-data-processing-saurabh-bhonsle
```

No external libraries or packages are required.

---

## Running the Program

### Using Windows Command Prompt

```bash
python reverse_string.py
```

### Using Visual Studio Code

1. Open the repository folder in VS Code.
2. Select a Python interpreter (Python 3.10 or above).
3. Open `reverse_string.py`.
4. Run the program using **Run Python File** or press **Ctrl + F5**.

### Using VS Code Terminal

```bash
python reverse_string.py
```

---

## Sample Output

### User Input

```text
Enter a string : Hello World

Original String : Hello World
Reversed String : dlroW olleH
```

### Hardcoded Input

```text
Original String : Hello World
Reversed String : dlroW olleH
```

---

## Complexity Summary

| Implementation | Time Complexity | Space Complexity |
|---------------|-----------------|------------------|
| OOP – User Input | O(n²) | O(n) |
| Function – Two Pointer | O(n) | O(n) |
| OOP – Hardcoded Input | O(n²) | O(n) |

---

## Notes

- The code is written in a clean and modular format.
- A separate `main()` function is used for program execution.
- Both Object-Oriented Programming and Function-Based approaches are demonstrated.
- The implementations are beginner-friendly and easy to understand.
