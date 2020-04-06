from itertools import permutations
from tqdm import tqdm

# INPUT WORD EQUATION HERE
equation_formed = ["KYOTO", "OSAKA","TOKYO" ]

all_alphabets_used = []
for element in equation_formed:
    alphabets_placed = list(element)
    for item in alphabets_placed:
        if item not in all_alphabets_used:
            all_alphabets_used.append(item)

single_digits = [ integer for integer in range(10)]

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
    print("---------------------------")

    word_string = ''
    for item in equation_formed[:-1]:
        word_string += item
        word_string += " + "

    word_string = word_string[:-2]
    word_string += '= ' + equation_formed[-1]
    print(word_string)

    number_string = ''
    for item in element[0][:-1]:
        number_string += str(item)
        number_string += " + "
    number_string = number_string[:-2]
    number_string += '= ' + str(element[0][-1])
    print(number_string)

    print(f"Paired values: {element[1]}\n")
