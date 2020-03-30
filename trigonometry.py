######################################################
##### [1] Generate Maclaurin series for tan(x)
######################################################

from fractions import Fraction

# INPUT HERE: How many non-zero terms do you want?
produce_terms = 15

tangent_coefficients = [ Fraction(1,1) ] 

def generate_the_next_coefficient():
    global tangent_coefficients
    how_many_terms = len(tangent_coefficients)
    reversed_coefficients = tangent_coefficients[::-1]

    final_sum = 0
    for integer in range(how_many_terms):
        final_sum += tangent_coefficients[integer] * reversed_coefficients[integer]

    tangent_coefficients.append(final_sum /(how_many_terms * 2 + 1))

for integer in range(produce_terms - 1):
    generate_the_next_coefficient()


tangent_coefficients.pop(0)
# Print results
print(f"\nThe first {produce_terms} number of non-zero terms of the Maclaurin series of tan(x) is\n\ntan(x) = x + ", end= '')

x_power = 3
for element in tangent_coefficients:
    print(f"({element.numerator}/{element.denominator})x^{x_power} +", end= ' ')
    x_power += 2
print("...\n")
