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
