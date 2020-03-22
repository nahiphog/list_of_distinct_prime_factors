######################################################
##### [1] Digital Sum
######################################################
from eulerlib.numtheory import *
print( digital_sum(input_number) )

######################################################
##### [2] Digital Root
######################################################
from eulerlib.numtheory import *
print( digital_root(input_number) )

######################################################
###### [3A] Is it a palindome (in default base 10)?
######################################################
def is_it_a_palindrome(input_number):
    paste_it_here = str(input_number)
    if paste_it_here == str(paste_it_here)[::-1]:
        return True
    else:
        return False
        
######################################################
###### [3B] Is it a palindome in some specific base?
######################################################
from eulerlib.etc import *
print( is_palindrome (input_number_base_10 , base) )
        
######################################################
##### [4] Convert to different number base
######################################################
from eulerlib.etc import *
print( decimal_to_base (input_number_base_10 , base) )

######################################################
##### [5] Is it pandigital (it only contains all the digits from 1 til 9)?
######################################################
from eulerlib.etc import *
input_number_here = 10000
starting_digit = 1
stopping_digit = 9
print ( def is_pandigital(num,starting_digit,stopping_digit) )

######################################################
##### [6] Convert the word into sum of numerical value of each letter in the word based on its position in the alphabet.
######################################################
from eulerlib.etc import *
print ( word_numerical_val('randomword') )

######################################################
##### [7] Pell's equation solution
######################################################
# Generate the first first solutions for Pell's equation x^2 - N * y^2 = 1 for a given positive integer N
from math import sqrt, floor
from tabulate import tabulate

# INPUT HERE: From x^2 - N * y^2 = 1
n = 29
# INPUT HERE: Print how many solutions? 
desired_solutions = 10

integer_part_of_sqrt_n = int( sqrt(n) )
generate_continued_fraction_list = []
modify_this_number = sqrt(n) - integer_part_of_sqrt_n
for index in range(30):
    use_this_number  = modify_this_number ** -1
    generate_continued_fraction_list.append( floor(use_this_number ) )
    modify_this_number = use_this_number - floor(use_this_number)

how_long_is_this_list = len(generate_continued_fraction_list)

numerator_list = [ 1 , generate_continued_fraction_list[1] ]
denominator_list = [ generate_continued_fraction_list[0] , generate_continued_fraction_list[0] * generate_continued_fraction_list[1] + 1 ]
generate_continued_fraction_list.pop(0)
generate_continued_fraction_list.pop(0)
while len(generate_continued_fraction_list) > 0:
    use_this_number = generate_continued_fraction_list.pop(0)
    numerator_list.append( use_this_number * numerator_list[-1] + numerator_list[-2] )
    denominator_list.append( use_this_number * denominator_list[-1] + denominator_list[-2] )

x_solution, y_solution = [] , []
# Find the fundamental solution
for element in range(how_long_is_this_list): 
    x = numerator_list[element] + integer_part_of_sqrt_n * denominator_list[element]
    y = denominator_list[element]
    if (x ** 2) - n * (y ** 2) == 1:
        x_solution.append(x)
        y_solution.append(y)
        break

# Use recurrence relation to generate more Pell's solution
for index in range(desired_solutions):
    x_last_solution = x_solution[-1]
    y_last_solution = y_solution[-1]

    x_solution.append( x_solution[0] * x_last_solution + n * y_solution[0] * y_last_solution )
    y_solution.append( x_solution[0] * y_last_solution + y_solution[0] * x_last_solution )

print_this_table = [[element + 1 , x_solution[element] , y_solution[element] ] for element in range(desired_solutions) ]

# Output solution
print(f"\nThe first {desired_solutions} solutions to the Pell's equation [ x^2 - {n} y^2 = 1 ] are:\n\n" +  
    tabulate(print_this_table, ["Index", "x", "y"], tablefmt="fancy_grid" , colalign=("right",)) )



print(convert_to_numeral(1000))


