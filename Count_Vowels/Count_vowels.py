"""
------------------------------------------------------------
EMBED SQUARE SOLUTIONS PRIVATE LIMITED
Python Programming Assessment - Strings & Data Processing

Program Title   : Count Vowels using OOP (User Input)
Author          : Saurabh Ravindra Bhonsle
Date            : 26 August 2026

Description:
This program counts the total number of vowels entered by
the user using Object-Oriented Programming (Class and Object).

Class Name      : StringOperations
Function Name   : count_vowels()
Argument        : text (String)
Returns         : Total Number of Vowels

Time Complexity : O(n)
Space Complexity: O(1)
------------------------------------------------------------
"""

class StringOperations:

    def count_vowels(self, text):
        count = 0

        for character in text.lower():
            if character in "aeiou":
                count = count + 1

        return count


def main():
    value = input("Enter a string : ").strip()

    if value == "":
        print("Input string is empty.")
        return

    obj = StringOperations()

    result = obj.count_vowels(value)

    print("Original String :", value)
    print("Total Vowels    :", result)


if __name__ == "__main__":
    main()

# End


# ------------------------------------------------------------
# EMBED SQUARE SOLUTIONS PRIVATE LIMITED
# Python Programming Assessment - Strings & Data Processing

# Program Title   : Count Vowels using Function (User Input)
# Author          : Saurabh Ravindra Bhonsle
# Date            : 26 August 2026

# Description:
# This program counts the total number of vowels entered by
# the user using Function Calling.

# Function Name   : count_vowels()
# Argument        : text (String)
# Returns         : Total Number of Vowels

# Time Complexity : O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------

# def count_vowels(text):
#     count = 0

#     for character in text.lower():
#         if character in "aeiou":
#             count = count + 1

#     return count


# def main():
#     value = input("Enter a string : ").strip()

#     if value == "":
#         print("Input string is empty.")
#         return

#     result = count_vowels(value)

#     print("Original String :", value)
#     print("Total Vowels    :", result)


# if __name__ == "__main__":
#     main()

# End


# ------------------------------------------------------------
# EMBED SQUARE SOLUTIONS PRIVATE LIMITED
# Python Programming Assessment - Strings & Data Processing

# Program Title   : Count Vowels using OOP (Hardcoded Input)
# Author          : Saurabh Ravindra Bhonsle
# Date            : 26 August 2026

# Description:
# This program counts the total number of vowels in a
# predefined string using Object-Oriented Programming.

# Class Name      : StringOperations
# Function Name   : count_vowels()
# Argument        : text (String)
# Returns         : Total Number of Vowels

# Time Complexity : O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------

# class StringOperations:

#     def count_vowels(self, text):
#         count = 0

#         for character in text.lower():
#             if character in "aeiou":
#                 count = count + 1

#         return count


# def main():

#     value = "Hello World"

#     obj = StringOperations()

#     result = obj.count_vowels(value)

#     print("Original String :", value)
#     print("Total Vowels    :", result)


# if __name__ == "__main__":
#     main()

# End



# New
# ------------------------------------------------------------
# EMBED SQUARE SOLUTIONS PRIVATE LIMITED
# Python Programming Assessment - Strings & Data Processing

# Program Title   : Count Vowels using OOP (User Input)
# Author          : Saurabh Ravindra Bhonsle
# Date            : 26 August 2026

# Description:
# This program counts the total number of vowels entered by
# the user using Object-Oriented Programming.

# Class Name      : CountVowels
# Main Class      : Main
# Function Name   : count_vowels()
# Argument        : text (String)
# Returns         : Total Number of Vowels

# Time Complexity : O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------
# """

# class CountVowels:

#     def count_vowels(self, text):
#         count = 0

#         for character in text.lower():
#             if character in "aeiou":
#                 count = count + 1

#         return count


# class Main:

#     def main(self):
#         value = input("Enter a string : ").strip()

#         if value == "":
#             print("Input string is empty.")
#             return

#         obj = CountVowels()

#         result = obj.count_vowels(value)

#         print("Original String :", value)
#         print("Total Vowels    :", result)


# if __name__ == "__main__":
#     obj = Main()
#     obj.main()
# End