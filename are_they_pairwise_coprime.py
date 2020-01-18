def are_they_pairwise_coprime(input_first_number, input_second_number):
    minimum_of_these_numbers = min(input_first_number, input_second_number)

    continue_testing = True

    test_this_integer = 2
    while test_this_integer <= minimum_of_these_numbers and (continue_testing):
        if input_first_number % test_this_integer == 0 and input_second_number % test_this_integer == 0:
            continue_testing = False
            break
        
        test_this_integer += 1

    return continue_testing

print(are_they_pairwise_coprime(12,23))
