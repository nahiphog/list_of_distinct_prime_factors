from itertools import permutations
from tqdm import tqdm
from tabulate import tabulate

# INPUT WORD EQUATION HERE, THE SYMBOLS '+' AND '=' ARE NOT MANDATORY
input_text_here = ' KYOTO + oSAKA = TOKYO '
text = input_text_here.strip().split()
for element in text:
    if not( element.isalpha() ):
        text.remove(element)
equation_formed = [ element.upper() for element in text ]

all_alphabets_used = []
for element in equation_formed:
    alphabets_placed = list(element)
    for item in alphabets_placed:
        if item not in all_alphabets_used:
            all_alphabets_used.append(item)

single_digits = [ integer for integer in range(10)]

word_string = ''
for item in equation_formed[:-1]:
    word_string += item
    word_string += " + "

word_string = word_string[:-2]
word_string += '= ' + equation_formed[-1]
print(f"The input is:\t {word_string}\n")

continue_experiment = True
if len(all_alphabets_used) > 10:
    print("Too many distinct letters were used. No solution formed.")
    stop_experiment = False

numerical_outputs = []

if continue_experiment == True: 
    solution_found = 0
    for specific_permutation in tqdm(list(permutations(single_digits, len(all_alphabets_used)))):
        pairing_values = [ [all_alphabets_used[i] , specific_permutation[i] ] for i in range(len(all_alphabets_used))]

        numbers_formed = []
        for words_found in equation_formed:
            join_this = ''
            for element in list(words_found):
                for item in pairing_values:
                    if item[0] == element:
                        element = item[1]
                        break
                join_this += str(element)
            numbers_formed.append(int(join_this))

        length_of_each_words = [ len(list(these_words)) for these_words in equation_formed ]
        length_of_each_numbers = [ len(list(str(these_numbers))) for these_numbers in numbers_formed ]
        
        if length_of_each_words == length_of_each_numbers:
            if sum(numbers_formed) == 2 * numbers_formed[-1]:
                numerical_outputs.append([numbers_formed, pairing_values])
                solution_found += 1

# Display results
print(f"Solutions found:\t {len(numerical_outputs)}\n")
solution_number = 0
for element in numerical_outputs:
    solution_number += 1
    print(f"Solution [{solution_number}]")
    print("---------------------------\n")

    number_string = ''
    for item in element[0][:-1]:
        number_string += str(item)
        number_string += " + "
    number_string = number_string[:-2]
    number_string += '= ' + str(element[0][-1])
    print(number_string)

    used_alphabets = [ element[1][i][0] for i in range(len(element[1])) ]
    used_values = [ element[1][i][1] for i in range(len(element[1])) ]
    table_of_alphabet_values = [ used_alphabets, used_values]
    print("Paired values:\n" + tabulate(table_of_alphabet_values, tablefmt="grid") + "\n")
