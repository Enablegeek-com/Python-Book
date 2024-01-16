def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divisible by 400, hence a leap year
            else:
                return False  # Divisible by 100 but not by 400, not a leap year
        else:
            return True  # Divisible by 4 but not by 100, hence a leap year
    else:
        return False  # Not divisible by 4, not a leap year.

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")