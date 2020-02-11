
######################################################
###### [1A] List all the primes from 1 til N inclusive via Sieve of Eratosthenes
######################################################
from eulerlib.prime_numbers import *
print_primes_up_to_this_number = 100
print( primes(print_primes_up_to_this_number) )
# OR
print( eulerlib.list_primes(print_primes_up_to_this_number) )

######################################################
###### [1B] List all the primes from 1 til N inclusive via Wheel factorization
######################################################
from eulerlib.prime_numbers import *
print_primes_up_to_this_number = 100
print( primes_wheel_fact(print_primes_up_to_this_number) )

######################################################
###### [2A] Is it a prime number? (Without library)
######################################################
def is_it_prime(input_number_here):
    well_is_it_prime_or_not = True
    i = 2
    while i <= (int(pow(input_number_here , 1/2)) + 1):

        if input_number_here == 2:
            well_is_it_prime_or_not = True
        elif input_number_here % i == 0:
            well_is_it_prime_or_not = False
        else:
            pass
        i += 1
            
    return well_is_it_prime_or_not

######################################################
###### [2B] Is it a prime number? (With library)
######################################################
from eulerlib.prime_numbers import *
print( is_prime(input_number_here) )

######################################################
###### [3] List of all distinct prime factors
######################################################
def list_of_distinct_prime_factors(given_number):
    list_of_prime_factors = []
    smallerize_this = given_number
    while smallerize_this > 1:
        if smallerize_this == 1:
            break
        elif smallerize_this == 2:
            list_of_prime_factors.append(2)
            break
        else:
            test_this_divisor = 2          
            while smallerize_this >= test_this_divisor:
                while smallerize_this % test_this_divisor == 0:
                    smallerize_this = int(smallerize_this / test_this_divisor)
                    list_of_prime_factors.append(test_this_divisor)
                test_this_divisor += 1
    
    return list(dict.fromkeys(list_of_prime_factors))

######################################################
###### [4A] Prime Factorization nice output
######################################################
factorize_this_number = 2137458620009 # Input number here

def prime_factorization(given_number):
    list_of_prime_factors = []
    smallerize_this = given_number

    # Find all the prime factors and their respective powers
    while smallerize_this > 1:
        if smallerize_this == 1:
            break
        elif smallerize_this == 2:
            list_of_prime_factors.append(2)
            break
        else:
            test_this_divisor = 2
            
            while smallerize_this >= test_this_divisor:
                while smallerize_this % test_this_divisor == 0:
                    smallerize_this = int(smallerize_this / test_this_divisor)
                    list_of_prime_factors.append(test_this_divisor)
                test_this_divisor += 1

    # Only keep distinct prime factors
    list_of_distinct_prime_factors = list(dict.fromkeys(list( list_of_prime_factors )))

    # Only list the powers of these distint prime factors
    power_listing = []
    for element in list_of_distinct_prime_factors:
        power_listing.append([ element, list_of_prime_factors.count(element) ] )
    
    # Display output part
    final_output = ""
    for element in power_listing:
        if element[1] == 1:
            final_output += str(element[0]) + " x "
        else:
            final_output += str(element[0]) + "^" + str(element[1]) + " x "

    return final_output[:-3]

# Display output
print(f"The prime factorization of {factorize_this_number} is:\n\n{ prime_factorization(factorize_this_number) }\n")

######################################################
###### [4B] Prime Factorization list output
######################################################
factorize_this_number = 2137458620009 # Input number here

def prime_factorization(given_number):
    list_of_prime_factors = []
    smallerize_this = given_number

    # Find all the prime factors and their respective powers
    while smallerize_this > 1:
        if smallerize_this == 1:
            break
        elif smallerize_this == 2:
            list_of_prime_factors.append(2)
            break
        else:
            test_this_divisor = 2
            
            while smallerize_this >= test_this_divisor:
                while smallerize_this % test_this_divisor == 0:
                    smallerize_this = int(smallerize_this / test_this_divisor)
                    list_of_prime_factors.append(test_this_divisor)
                test_this_divisor += 1

    # Only keep distinct prime factors
    list_of_distinct_prime_factors = list(dict.fromkeys(list( list_of_prime_factors )))

    # Only list the powers of these distint prime factors
    power_listing = []
    for element in list_of_distinct_prime_factors:
        power_listing.append([ element, list_of_prime_factors.count(element) ] )

    return power_listing
    
######################################################
###### [5] Euler Totient function
######################################################
def euler_totient_function(given_number):
    # Figure out all the prime factors first
    list_of_prime_factors = []
    smallerize_this = given_number
    while smallerize_this > 1:
        if smallerize_this == 1:
            break
        elif smallerize_this == 2:
            list_of_prime_factors.append(2)
            break
        else:
            test_this_divisor = 2
            while smallerize_this >= test_this_divisor:
                while smallerize_this % test_this_divisor == 0:
                    smallerize_this = int(smallerize_this / test_this_divisor)
                    list_of_prime_factors.append(test_this_divisor)
                test_this_divisor += 1
    # Only keep distinct prime factors
    list_of_prime_factors = list(dict.fromkeys(list(list_of_prime_factors)))
    # Apply the Euler Totient Function formula
    product = given_number
    for element in list_of_prime_factors:
        product *= (1 - 1/element)
    return int(product)
    
    
######################################################
###### [6A] Arithmetic Derivative function (looping)
######################################################
from eulerlib.prime_numbers import *

def arithmetic_derivative_function(input_number_here):
    if is_prime(input_number_here):
        return 1

    else:
        # Find the smallest prime factors of this number
        smallerize_this = input_number_here
        divided_by = 0
        while divided_by == 0:
            test_this_divisor = 2          
            while smallerize_this >= test_this_divisor:
                if smallerize_this % test_this_divisor == 0:
                    divided_by = int(smallerize_this / test_this_divisor)
                    break
                else:
                    test_this_divisor += 1

        return test_this_divisor * arithmetic_derivative_function(divided_by) + divided_by
        
######################################################
###### [6B] Arithmetic Derivative function (Leibniz Rule)
######################################################
def arithmetic_derivative_function(input_number_here):
    list_of_prime_factors = []
    smallerize_this = input_number_here

    # Find all the prime factors and their respective powers
    while smallerize_this > 1:
        if smallerize_this == 1:
            break
        elif smallerize_this == 2:
            list_of_prime_factors.append(2)
            break
        else:
            test_this_divisor = 2
            
            while smallerize_this >= test_this_divisor:
                while smallerize_this % test_this_divisor == 0:
                    smallerize_this = int(smallerize_this / test_this_divisor)
                    list_of_prime_factors.append(test_this_divisor)
                test_this_divisor += 1

    reciprocal_sum = 0
    for element in list_of_prime_factors:
        reciprocal_sum += 1/element

    return int ( input_number_here * reciprocal_sum )
    
######################################################
###### [7A] Prime omega function https://en.wikipedia.org/wiki/Prime_omega_function
###################################################### (count the number of prime factors with multiplicity)
def prime_omega_function(given_number):
    list_of_prime_factors = []
    smallerize_this = given_number
    while smallerize_this > 1:
        if smallerize_this == 1:
            break
        elif smallerize_this == 2:
            list_of_prime_factors.append(2)
            break
        else:
            test_this_divisor = 2          
            while smallerize_this >= test_this_divisor:
                while smallerize_this % test_this_divisor == 0:
                    smallerize_this = int(smallerize_this / test_this_divisor)
                    list_of_prime_factors.append(test_this_divisor)
                test_this_divisor += 1
    
    return len(list_of_prime_factors)
    
######################################################
###### [7B] Little Prime omega function https://en.wikipedia.org/wiki/Prime_omega_function
###################################################### (count the distinct number of prime factors)

def little_prime_omega_function(given_number):
    list_of_prime_factors = []
    smallerize_this = given_number
    while smallerize_this > 1:
        if smallerize_this == 1:
            break
        elif smallerize_this == 2:
            list_of_prime_factors.append(2)
            break
        else:
            test_this_divisor = 2          
            while smallerize_this >= test_this_divisor:
                while smallerize_this % test_this_divisor == 0:
                    smallerize_this = int(smallerize_this / test_this_divisor)
                    list_of_prime_factors.append(test_this_divisor)
                test_this_divisor += 1
    
    return len(list(dict.fromkeys(list_of_prime_factors)))
    
######################################################
###### [7C] Liouville function https://en.wikipedia.org/wiki/Liouville_function
######################################################
def liouville_function(given_number):
    list_of_prime_factors = []
    smallerize_this = given_number
    while smallerize_this > 1:
        if smallerize_this == 1:
            break
        elif smallerize_this == 2:
            list_of_prime_factors.append(2)
            break
        else:
            test_this_divisor = 2          
            while smallerize_this >= test_this_divisor:
                while smallerize_this % test_this_divisor == 0:
                    smallerize_this = int(smallerize_this / test_this_divisor)
                    list_of_prime_factors.append(test_this_divisor)
                test_this_divisor += 1
    
    return pow( -1, len(list_of_prime_factors) )


######################################################
###### [7D] Möbius function https://en.wikipedia.org/wiki/M%C3%B6bius_function
######################################################
def mobius_function(given_number):
    list_of_prime_factors = []
    smallerize_this = given_number

    # Find all the prime factors and their respective powers
    while smallerize_this > 1:
        if smallerize_this == 1:
            break
        elif smallerize_this == 2:
            list_of_prime_factors.append(2)
            break
        else:
            test_this_divisor = 2
            
            while smallerize_this >= test_this_divisor:
                while smallerize_this % test_this_divisor == 0:
                    smallerize_this = int(smallerize_this / test_this_divisor)
                    list_of_prime_factors.append(test_this_divisor)
                test_this_divisor += 1

    # Only keep distinct prime factors
    list_of_distinct_prime_factors = list(dict.fromkeys(list( list_of_prime_factors )))

    # Only list the powers of these distint prime factors
    power_listing = []
    for element in list_of_distinct_prime_factors:
        power_listing.append([ element, list_of_prime_factors.count(element) ] )

    product_of_powers = 1
    for power in power_listing:
        product_of_powers *= power[1]

    if product_of_powers % 2 == 0:
        return 0
    
    else:
        if len(power_listing) % 2 == 0:
            return 1
        else:
            return -1
