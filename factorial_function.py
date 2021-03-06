######################################################
##### [1A] Calculate the factorial of non-negative integer N, N! (No library)
######################################################
def factorialize_this(input_integer):
    if input_integer == 0:
        return 1
    else:
        return input_integer * factorialize_this(input_integer - 1)
        
######################################################
##### [1B] Calculate the factorial of non-negative integer N, N! (With library)
######################################################
from math import factorial
print( factorial(input_number_here) )

######################################################
##### [2A] Find the combination, binom(n,r)
######################################################
from eulerlib.numtheory import *
top,bottom = 10, 5 # INPUT VALUES HERE
print( nCr( top , bottom ) )

######################################################
##### [2B] Find the permutation, perm(n,r)
######################################################
from eulerlib.numtheory import *
top,bottom = 10, 5 # INPUT VALUES HERE
print( nPr( top , bottom ) )

######################################################
##### [3] de Polignac's formula https://en.wikipedia.org/wiki/Legendre%27s_formula
######################################################
import math
def number_of_trailing_zeroes(number_factorial):
    upper_sum = math.floor( math.log(number_factorial, 5) )
    return sum( math.floor( number_factorial / (5 ** k)) for k in range(1, upper_sum +1 ) )
    
    
######################################################
##### [4] Half factorials
######################################################
from fractions import Fraction as frac
import math
give_me_half_integer = 12.5 # INPUT VALUE HERE
pi = 3.1415926535897932384626433832795028

def product_in_the_list(give_me_list):
    result = 1
    for element in give_me_list:
        result *= element
    return result

top = [ integer for integer in range(1, int(2 * give_me_half_integer) + 1, 2) ]
bottom = 2 ** (math.ceil(give_me_half_integer))

print(frac( product_in_the_list(top) , bottom ), " * sqrt(pi)" , "\nApproximation:\t\t", product_in_the_list(top) / bottom * pow(pi , 1/2) )
