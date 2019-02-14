import math

int_1 = 10
float_1 = 3.14
bool_1 = True
word = "Python"

#Task 2
number_1 = int_1 + 6.5 # mathematical addition operation
number_2 = int_1 - 1.9 # mathematical operation taking away
number_3 = int_1 / 2 # mathematical operation division
number_4 = int_1 * 10.1 #mathematical operation multiplication

print ("Task 2", number_1, number_2, number_3, number_4, sep='\n')

# Task 3
int_2 = math.pow(-2, 2) # Examination to the degree using the library math
int_3 = -2 ** 2 # mathematical operation of exponentiation

print ("Task 3", int_2, int_3, sep='\n')

# Task 4
int_4 = math.sqrt(121)
int_5 = -121 ** 0.5

print ("Task 4", int_4, int_5, sep='\n')

# Task 5
float_2 = float(int_1) # convert an integer to a floating point number
int_6 = int(float_1) # convert floating-point number to integer
bool_2 = bool(int_1) # checking the int_1 variable for truth
int_7 = int(bool_2)

print ("Task 5", float_2, int_6, bool_2, int_7, sep='\n')

# Task 6
number_5 = 10 / 3
rounding_1 = round(number_5, 2) # rounding to two digits after the floating point with the command
rounding_2 = '{0:.{1}f}'.format(number_5, 2) # rounding to two digits after a floating point using a string format

print ("Task 6", number_5, rounding_1, rounding_2, sep='\n')
