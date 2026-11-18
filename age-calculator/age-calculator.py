current_year = 2026
birth_year = int(input("Enter your birth year: "))  # I chose to do int as an integer to ensure the input is a number as it starts out being a string. This way, we can perform arithmetic operations on it without any issues.


if birth_year > 1900 and birth_year <= current_year:
    age = current_year - birth_year
    print(f"You are approximately {age} years old.") # I did a f string to make it easier and simpler.
else:
    print("Birth year is invalid, enter a valid birth year.")

