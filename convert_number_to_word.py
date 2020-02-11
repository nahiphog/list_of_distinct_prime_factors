# Do this first: https://pypi.org/project/num2words/
from num2words import num2words

the_number_to_print = 1234567

def commify(n):
    if n is None: return None
    n = str(n)
    if '.' in n:
        dollars, cents = n.split('.')
    else:
        dollars, cents = n, None

    r = []
    for i, c in enumerate(str(dollars)[::-1]):
        if i and (not (i % 3)):
            r.insert(0, ',')
        r.insert(0, c)
    out = ''.join(r)
    if cents:
        out += '.' + cents
    return out

print("\n" + 
    f"[1A] The input number:\t\t\t{the_number_to_print} \n" + 
    f"[1B] The input number with commas:\t{commify(the_number_to_print)} \n" + 
    f"[2] In words:\t\t\t\t{ num2words(the_number_to_print) } \n" + 
    f"[3] In cardinals:\t\t\t{num2words(the_number_to_print, to='ordinal') } \n" + 
    f"[4] In year:\t\t\t\t{num2words(the_number_to_print, to='year') }\n" + 
    f"[5] In cents:\t\t\t\t{num2words(the_number_to_print, to='currency') }\n"
    )

### RESULTS
# [1A] The input number:                  1234567
# [1B] The input number with commas:      1,234,567
# [2] In words:                           one million, two hundred and thirty-four thousand, five hundred and sixty-seven
# [3] In cardinals:                       one million, two hundred and thirty-four thousand, five hundred and sixty-seventh
# [4] In year:                            one million, two hundred and thirty-four thousand, five hundred and sixty-seven
# [5] In cents:                           twelve thousand, three hundred and forty-five euro, sixty-seven cents
