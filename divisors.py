  ######################################################
###### [1A] List of divisors
######################################################
def list_of_divisors(input_number_here):
    return [ verified_divisor for verified_divisor in range(1, input_number_here + 1) if input_number_here % verified_divisor == 0 ]


######################################################
###### [1B] Calculate the total number of positive divisors of a positive integer input, including 1 and itself
######################################################
def number_of_divisors(input_number_here):
    frequency = 0
    
    if input_number_here == 1:
        return 1
    else:
        for test_integer in range(1, input_number_here + 1):
            if input_number_here % test_integer == 0:
                frequency += 1
            else:
                pass
        return frequency
        
######################################################
###### [1C] Calculate the number of proper divisors         
######################################################
def number_of_proper_divisors(input_number_here):
    if input_number_here < 3:
        return input_number_here - 1
    else:
        return number_of_divisors(input_number_here) - 2
        
######################################################
###### [2A] Sum of divisors, sigma_1 (x)
######################################################
def sum_of_of_divisors(input_number_here):
    frequency = 0
    
    if input_number_here == 1:
        return 1
    else:
        for test_integer in range(1, input_number_here + 1):
            if input_number_here % test_integer == 0:
                frequency += test_integer
            else:
                pass
        return frequency

######################################################
###### [2B] Sum of powers of divisors, sigma_n (x)
######################################################
def sum_of_powers_of_divisors(input_number_here, raise_to_the_power):
    frequency = 0
    
    if input_number_here == 1:
        return 1
    else:
        for test_integer in range(1, input_number_here + 1):
            if input_number_here % test_integer == 0:
                frequency += pow(test_integer, raise_to_the_power)
            else:
                pass
        return frequency
        
######################################################
###### [3] List of unitary divisors https://en.wikipedia.org/wiki/Unitary_divisor
######################################################
from eulerlib.numtheory import *
def list_of_unitary_divisors(input_number_here):
    return [ verified_divisor for verified_divisor in range(1, input_number_here + 1) if (input_number_here % verified_divisor == 0) and gcd(verified_divisor, input_number_here // verified_divisor ) == 1]


