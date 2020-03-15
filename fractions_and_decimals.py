######################################################
###### [1A] Simplify this fraction and convert this decimal to fraction
######################################################
from fractions import Fraction as frac
print(frac(-45, 54)) # -5/6
print(frac('3.14159265359')) # 314159265359/100000000000

######################################################
###### [1B] Simplify this fraction, but only display the numerator/denominator
######################################################
from fractions import Fraction as frac
print(frac('36.25').numerator) # 145
print(frac('36.25').denominator) # 4

######################################################
###### [3] Approximate this fraction, but set a limiting denominator
######################################################
from fractions import Fraction as frac
print(frac(3.14159265359).limit_denominator(1000)) # 355/113

######################################################
###### [4] Convert this decimal to fraction
######################################################
from fractions import Fraction
from decimal import Decimal
print( Fraction(Decimal('1.1')) )

######################################################
###### [5] Get more decimal places
######################################################
from decimal import *
getcontext().prec = 100

numerator = 6302553750017181976885708596439350657917328836576210147657113954921484651315312300767967432581025858455759276513304553523392669590219116606086594984025733
denominator = 1284818119838213405756315260059047204398389394375816015329163156623582078083657717559313924216917551084967127979654735160558454575333744643714247390793231

print(Decimal(numerator / denominator))

######################################################
###### [6] Generate convergent continued fractions
######################################################
# For simplicity sake, assume the number is in the range (0,1)

# Input here, make sure to have at least 2 elements
continued_fraction_listing = [3, 3, 9, 2, 2, 4, 6, 2, 1, 1, 3, 1, 18]

how_long_is_this_list = len(continued_fraction_listing)

numerator_list = [ 1 , continued_fraction_listing[1] ]
denominator_list = [ continued_fraction_listing[0] , continued_fraction_listing[0] * continued_fraction_listing[1] + 1 ]

continued_fraction_listing.pop(0)
continued_fraction_listing.pop(0)

while len(continued_fraction_listing) > 0:
    use_this_number = continued_fraction_listing.pop(0)
    numerator_list.append( use_this_number * numerator_list[-1] + numerator_list[-2] )
    denominator_list.append( use_this_number * denominator_list[-1] + denominator_list[-2] )
    
for element in range(how_long_is_this_list): print(f"{numerator_list[element]}/{denominator_list[element]}" )
