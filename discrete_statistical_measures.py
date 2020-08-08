from fractions import Fraction as ff
from math import sqrt

def verify_valid_dpdf(dpdf):
    '''
    We want to make sure the input discrete probability density function (D PDF) is valid.
    It must satisfy (Sum = 1) and all of them are non-negative.
    '''
    sum_of_probabilities = sum( item[1] for item in dpdf)

    if not(sum_of_probabilities == 1): return False
    else: 
        if not(min( item[1] for item in dpdf) >= 0): return False
        else: return True

def raw_moment(dpdf, k):
    '''
    We want to compute the mathematical expectation, E[X^k] = sum_(domain) ( value^k * Pr[value] )
    '''
    return sum( ( item[0] ** k) * item[1] for item in dpdf )


def factorial_moment(dpdf, k):
    '''
    We want to compute the mathematical expectation, E[ X(X-1)(X-2) ... (X-k + 1)] 
    = sum_(domain) ( value(value-1)(value-2) ... (value-k + 1) * Pr[value] )
    '''
    def falling(n,k):
        if k == 0: return 1
        else: return n * falling(n-1,k-1)
    
    return sum( falling(item[0] , k) * item[1] for item in dpdf )


def population_variance(dpdf):
    '''
    Var[X] = E[X^2] - ( E[X] )^2
    '''
    second_raw_moment = raw_moment(dpdf, 2)
    first_raw_moment = raw_moment(dpdf, 1)

    return second_raw_moment - (first_raw_moment ** 2)

def absolute_moment(dpdf, k, a):
    '''
    We want to compute the mathematical expectation, E[ |X - a|^k ] = sum_(domain) ( |value - a|^k * Pr[value] )
    '''
    return sum( ( abs(item[0] - a) ** k) * item[1] for item in dpdf )

def central_moment(dpdf, k):
    '''
    We want to compute the mathematical expectation, E[  (X - E[X])^k ] = sum_(domain) (  (X - E[X])^k * Pr[value] )
    '''
    this_mean = raw_moment(dpdf, 1)

    return sum( ((item[0] - this_mean) ** k) * item[1] for item in dpdf )


def skewness_value(dpdf):
    '''
    Skewness = E[(X - mu)^3] / ( E[(X-mu)^2] )^(3/2)
    '''

    this_numerator = central_moment(dpdf, 3)
    this_denominator = (population_variance(dpdf)) ** (3/2)

    return this_numerator / this_denominator

def kurtosis_value(dpdf):
    '''
    Kurtosis = E[(X - mu)^4] / ( E[(X-mu)^2] )^2
    '''

    this_numerator = central_moment(dpdf, 4)
    this_denominator = (population_variance(dpdf)) ** 2

    return this_numerator / this_denominator

def coefficient_of_variation(dpdf):
    '''
    Compute standard deviation / mean
    '''
    return sqrt(population_variance(dpdf)) / raw_moment(dpdf, 1)

six_pdf = [
    [2, ff(2048,2 ** 17)],
    [3, ff(12288,2 ** 17)],
    [4, ff(16512,2 ** 17)],
    [5, ff(18432,2 ** 17)],
    [6, ff(20976,2 ** 17)],
    [7, ff(16464,2 ** 17)],
    [8, ff(14796,2 ** 17)],
    [9, ff(11220,2 ** 17)],
    [10, ff(7168,2 ** 17)],
    [11, ff(5172,2 ** 17)],
    [12, ff(3031,2 ** 17)],
    [13, ff(1495,2 ** 17)],
    [14, ff(831,2 ** 17)],
    [15, ff(407,2 ** 17)],
    [16, ff(161,2 ** 17)],
    [17, ff(57,2 ** 17)],
    [18, ff(13,2 ** 17)],
    [19, ff(1,2 ** 17)]
    ]

def print_results(dpdf):

    if verify_valid_dpdf(dpdf) == False:
        print("This is not a valid discrete probability distribution function.")

    else:
        this_mean = expectation1(dpdf)
        this_variance = variance_compute(dpdf)
    
        print(f"Mean:\t{this_mean} = {this_mean.numerator / this_mean.denominator} ")
        print(f"Population variance:\t{this_variance} = {this_variance.numerator / this_variance.denominator}")


print(skewness_value(three_pdf) ** 2)
