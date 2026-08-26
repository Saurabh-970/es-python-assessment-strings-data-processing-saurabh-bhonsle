# Count Vowels – Python Programming Assessment

## Candidate Information

**Name:** Saurabh Ravindra Bhonsle

**Role:** Python Developer Intern Assessment

**Company:** Embed Square Solutions Pvt. Ltd.

**Submission Date:** 26 August 2026

---

## Overview

This repository contains the solution for **Question 2 – Count Vowels** from the Python Programming Assessment conducted by Embed Square Solutions.

The program counts the total number of vowels present in a given string while handling both uppercase and lowercase characters.

---

## Problem Statement

Write a Python program that counts the number of vowels in a given string.

### Requirements

- Count vowels: `a, e, i, o, u`
- Handle both uppercase and lowercase characters.
- Return the total number of vowels present in the string.
- Handle empty string input gracefully.

---

## Implementations Included

This repository contains multiple implementations of the same problem.

| Implementation | Input Type | Time Complexity | Space Complexity |
|---------------|------------|-----------------|------------------|
| OOP (Class & Object) | User Input | O(n) | O(1) |
| Function Calling | User Input | O(n) | O(1) |
| OOP (Class & Object) | Hardcoded Input | O(n) | O(1) |
| OOP with Main Class | User Input | O(n) | O(1) |

---

## Approach

### OOP Approach

- Create a class `StringOperations`.
- Implement the `count_vowels()` method.
- Create an object inside `main()` and call the method.
- Display the original string and total vowel count.

### Function Calling Approach

- Create a function `count_vowels()`.
- Traverse the string character by character.
- Convert the string to lowercase.
- Count characters that belong to `a, e, i, o, u`.
- Return the total count.

### OOP with Main Class

- Create a separate `CountVowels` class for business logic.
- Create a `Main` class to handle user input and method invocation.
- This demonstrates modular Object-Oriented Programming.

---

## Test Cases Handled

| Input | Output |
|-------|--------|
| `Hello World` | `3` |
| `AEIOU` | `5` |
| `Python` | `1` |
| `rhythm` | `0` |
| `12345` | `0` |
| `@Hello123!` | `2` |
| Empty String (`""`) | `Input string is empty.` |

---

## Project Structure

```text
es-python-assessment-strings-data-processing-saurabh-bhonsle/
│
├── count_vowels.py
└── README.md
```

---

## Python Version

**Recommended Version:** Python 3.10 or above

Check your Python version:

```bash
python --version
```

or

```bash
python3 --version
```

---

## Installation

### Clone the Repository

```bash
git clone <repository-link>
```

### Open the Project Folder

```bash
cd es-python-assessment-strings-data-processing-saurabh-bhonsle
```

No external libraries or packages are required.

---

## How to Run

### Windows Command Prompt

```bash
python count_vowels.py
```

### Visual Studio Code

1. Open the project folder in VS Code.
2. Select Python 3.10 or above as the interpreter.
3. Open `count_vowels.py`.
4. Click **Run Python File** or press **Ctrl + F5**.

### VS Code Integrated Terminal

```bash
python count_vowels.py
```

---

## Sample Output

### User Input

```text
Enter a string : Hello World

Original String : Hello World
Total Vowels    : 3
```

### Hardcoded Input

```text
Original String : Hello World
Total Vowels    : 3
```

---

## Complexity Summary

| Implementation | Time Complexity | Space Complexity |
|---------------|-----------------|------------------|
| OOP – User Input | O(n) | O(1) |
| Function Calling | O(n) | O(1) |
| OOP – Hardcoded Input | O(n) | O(1) |
| OOP – Main Class | O(n) | O(1) |

---

## Notes

- The program uses clean and modular Python code.
- Separate implementations are provided using both Function Calling and Object-Oriented Programming.
- The solution handles uppercase and lowercase vowels correctly.
- Empty string input is validated before processing.
