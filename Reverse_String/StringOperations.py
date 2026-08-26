"""
------------------------------------------------------------
EMBED SQUARE SOLUTIONS PRIVATE LIMITED
Python Programming Assessment - Strings & Data Processing

Program Title   : Reverse String using OOP (User Input)
Author          : Saurabh Ravindra Bhonsle
Date            : 26 August 2026

Description:
This program reverses a string entered by the user using
Object-Oriented Programming (Class and Object).

Class Name      : StringOperations
Function Name   : reverse_string()
Argument        : text (String)
Returns         : Reversed String

Time Complexity : O(n²)
Space Complexity: O(n)
------------------------------------------------------------
"""

class StringOperations:

    def reverse_string(self, text):
        reverse = ""

        for character in text:
            reverse = character + reverse

        return reverse


def main():
    value = input("Enter a string : ").strip()

    if value == "":
        print("Input string is empty.")
        return

    obj = StringOperations()

    result = obj.reverse_string(value)

    print("Original String :", value)
    print("Reversed String :", result)


if __name__ == "__main__":
    main()
# End




# ------------------------------------------------------------
# EMBED SQUARE SOLUTIONS PRIVATE LIMITED
# Python Programming Assessment – Strings & Data Processing

# Program Title   : Reverse String using Function (Two Pointer)
# Author          : Saurabh Ravindra Bhonsle
# Date            : 26 August 2026

# Description:
# This program reverses a string entered by the user using
# the Two Pointer technique and Function Calling.

# Function Name   : reverse_string()
# Argument        : text (String)
# Returns         : Reversed String

# Time Complexity : O(n)
# Space Complexity: O(n)
# ------------------------------------------------------------

# def reverse_string(text):
#     characters = list(text)

#     start = 0
#     end = len(characters) - 1

#     while start < end:
#         characters[start], characters[end] = characters[end], characters[start]
#         start = start + 1
#         end = end - 1

#     reverse = "".join(characters)

#     return reverse


# def main():
#     value = input("Enter a string : ").strip()

#     if value == "":
#         print("Input string is empty.")
#         return

#     result = reverse_string(value)

#     print("Original String :", value)
#     print("Reversed String :", result)


# if __name__ == "__main__":
#     main()
# End

# ------------------------------------------------------------
# EMBED SQUARE SOLUTIONS PRIVATE LIMITED
# Python Programming Assessment – Strings & Data Processing

# Program Title   : Reverse String using OOP (Hardcoded Input)
# Author          : Saurabh Ravindra Bhonsle
# Date            : 26 August 2026

# Description:
# This program reverses a predefined string using
# Object-Oriented Programming (Class and Object).

# Class Name      : StringOperations
# Function Name   : reverse_string()
# Argument        : text (String)
# Returns         : Reversed String

# Time Complexity : O(n²)
# Space Complexity: O(n)
# ------------------------------------------------------------
# """

# class StringOperations:

#     def reverse_string(self, text):
#         reverse = ""

#         for character in text:
#             reverse = character + reverse

#         return reverse


# def main():

#     value = "Hello World"

#     obj = StringOperations()

#     result = obj.reverse_string(value)

#     print("Original String :", value)
#     print("Reversed String :", result)


# if __name__ == "__main__":
#     main()
# End
# """