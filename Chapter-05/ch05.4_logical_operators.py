x = 10
y = 5

is_valid = (x > 0) and (y < 10)
print(is_valid)  # Output: True

is_invalid = (x < 0) or (y > 10)
print(is_invalid)  # Output: False

is_false = not (x > 0)
print(is_false)  # Output: False