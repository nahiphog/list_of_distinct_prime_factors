####################################################################
################# SYSTEM OF LINEAR EQUATIONS
####################################################################
import sympy
# create the variables
a,b,c = sympy.var(['a','b','c'])
# write the equations, setting them all equal to zero
eqns = [  
a + 2 * b + 3 * c - 5,
7 * a + 11 * b + 13 * c - 17,
19 * a + 23 * b + 29 * c - 31
]
# solve the equations for the variables
print( sympy.solve(eqns, [a,b,c]) )
# {a: -35/18, b: 2/9, c: 13/6}

####################################################################
#### NEWTON's SUM, currently only works for 3rd degree polynomials
####################################################################
import sympy

number_of_variables = 3
display_power_until = 10

# Polynomial coefficients, written from left to right
poly_c = [1,5,-9,12]

# In ascending order
sum_of_powers = [number_of_variables]

def create_more_sum_of_powers(give_me_power):
    global sum_of_powers

    if give_me_power == 1:
        this_sum_of_powers =  -poly_c[1] / poly_c[0]
    
    elif give_me_power == 2:
        a,b = sympy.var(['a','b'])
        eqns = [  
        poly_c[0] * a + poly_c[1] * b  + 2 * poly_c[2],
        b - sum_of_powers[-1]
        ]
        this_sum_of_powers = ( sympy.solve(eqns, [a,b]).get(a) )

    elif give_me_power == 3:
        a,b,c = sympy.var(['a','b', 'c'])
        eqns = [  
        poly_c[0] * a + poly_c[1] * b + poly_c[2] * c + 3 * poly_c[3],
        b - sum_of_powers[-1],
        c - sum_of_powers[-2]
        ]
        this_sum_of_powers = ( sympy.solve(eqns, [a,b,c]).get(a) )


    elif give_me_power >= 4:
        a,b,c,d = sympy.var(['a','b','c', 'd'])
        eqns = [  
        poly_c[0] * a + poly_c[1] * b + poly_c[2] * c + poly_c[3] * d,
        b - sum_of_powers[-1],
        c - sum_of_powers[-2],
        d - sum_of_powers[-3]
        ]
        this_sum_of_powers =  sympy.solve(eqns, [a,b,c,d]).get(a)


    if int(this_sum_of_powers) == this_sum_of_powers:
        this_sum_of_powers = int(this_sum_of_powers)

    sum_of_powers.append(this_sum_of_powers)

for _ in range(1,display_power_until + 1):
    create_more_sum_of_powers(_)

for integer in range(0, display_power_until + 1):
    print(integer, sum_of_powers[integer])
