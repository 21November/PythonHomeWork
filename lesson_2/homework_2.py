import math

int_1 = -15
float_1 = 3.14
bool_1 = True
word = "Python"

#Task 2
number_1 = int_1 + 6.5   # Mathematical addition operation
number_2 = int_1 - 1.9   # Mathematical operation taking away
number_3 = int_1 / 2     # Mathematical operation division
number_4 = int_1 * 10.1  # Mathematical operation multiplication
number_5 = int_1 // 2    # This operation returns the integer result of the division, discarding the fractional part.
number_6 = int_1 ** 2    # Mathematical operation exponentiation
number_7 = int_1 % 2     # Getting the remainder of the division

print("Task 2", number_1, number_2, number_3, number_4, number_5, number_6, number_7, sep='\n')

# Task 3
int_2 = math.pow(-2, 2)  # Examination to the degree using the library math
int_3 = -2 ** 2          # Mathematical operation of exponentiation

print("Task 3", int_2, int_3, sep='\n')

# Task 4
int_4 = math.sqrt(121)
int_5 = -121 ** 0.5

print("Task 4", int_4, int_5, sep='\n')

# Task 5
float_2 = float(int_1)  # Convert an integer to a floating point number
int_6 = int(float_1)    # Convert floating-point number to integer
bool_2 = bool(int_1)    # Convert int_1 variable to a bool variable
int_7 = int(bool_2)     # Convert bool_2 variable to int variable

print("Task 5", float_2, int_6, bool_2, int_7, sep='\n')

# Task 6
number_5 = 10 / 3
rounding_1 = round(number_5, 2)                # Rounding to two digits after the floating point with the command
rounding_2 = '{0:.{1}f}'.format(number_5, 2)   # Rounding to two digits after a floating point using a string format
rounding_3 = f"{number_5:.2f}"                 # Rounding up to two digits after a floating-point number using the f-string method

print ("Task 6", number_5, rounding_1, rounding_2, rounding_3, sep='\n')

# region comments for homework iteration #1
# TODO: 1) Common issue 1 space before line comment. Please read PEP8.
# TODO: 2) Common issue space after print function name and before round braces of function. Please read PEP8
# TODO: 3) Task #2 Not all arithmetic operations present(modulus and Floor division)
# TODO: 4) Line 31 - confusing comment, Line 32 comment for customization is not present.
# endregion