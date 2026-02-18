age = int(input("Enter your age: "))
"""
decades.py
Module-level docstring for a small script that computes and prints a person's age
expressed in decades.
Description:
    Prompts the user to enter their age (expected to be an integer) and prints:
      - the age in decades as a floating-point value,
      - the number of full decades completed (integer),
      - the number of years into the current decade (remainder).
Usage:
    Run the script and enter an integer when prompted. Example:
        $ python decades.py
        Enter your age: 34
        You are 3.4 decades old.
        You are 3 full decades old.
        You have lived 4 years into your current decade.
Notes:
    - The script converts the input to int; invalid (non-numeric) input will raise ValueError.
    - Negative ages are handled numerically but are likely semantically invalid for this context.
    - The implementation uses normal division (/) for fractional decades, floor division (//)
      for full decades, and modulus (%) for the remainder years.
"""
decades = age / 10
print("You are", decades, "decades old.")

decades = age // 10
print("You are", decades, "full decades old.")

decades_remainder = age % 10
print("You have lived", decades_remainder, "years into your current decade.")
