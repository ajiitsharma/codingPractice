#!/bin/python3
import math
from fractions import Fraction
from decimal import Decimal, getcontext

def best_fractions_bruteforce(left: int, right: int) -> tuple:

        min_max = list(map(lambda x: (x, math.floor(math.pi*x), math.ceil(math.pi*x)), range(left,right+1)))
        best_for_denom = list(map(lambda x: (x[0], x[1]) if abs(math.pi-x[2]/x[0]) > abs(math.pi - x[1]/x[0])  else (x[0], x[2]), min_max))
        best_in_set = list(map(lambda x: abs(math.pi - x[1]/x[0]), best_for_denom))
        best_frac = best_for_denom[best_in_set.index(min(best_in_set))]

        return best_frac

def continued_fraction_pi(n_terms):
        """
        Generates the first n_terms of the continued fraction expansion of pi.
        """
        getcontext().prec = 100 # Set precision for Decimal calculations
        pi_dec = Decimal(math.pi)
        terms = []
        
        # Calculate integer part
        integer_part = int(pi_dec)
        terms.append(integer_part)
        
        # Calculate fractional parts
        remainder = pi_dec - integer_part
        for _ in range(n_terms - 1):
                if remainder == 0:
                        break
                reciprocal = Decimal(1) / remainder
                integer_part = int(reciprocal)
                terms.append(integer_part)
                remainder = reciprocal - integer_part
                
        return terms

def find_best_approximation(a, b):
        """
        Finds the best rational approximation of pi with a denominator
        in the range [a, b].
        """
        # The number of terms in the continued fraction needed for
        # a given maximum denominator is logarithmic. We can
        # safely use a large enough number of terms.
        n_terms = 50 
        cf_terms = continued_fraction_pi(n_terms)
        
        best_p, best_q = -1, -1
        min_error = float('inf')
        
        # Initialize with the first convergent
        p0, q0 = Fraction(cf_terms[0]), 1
        
        # Check if the initial terms are in the range
        if a <= q0 <= b:
                error = abs(p0 - math.pi)
                if error < min_error:
                        min_error = error
                        best_p, best_q = p0, q0
        
        # Initialize for recurrence relation
        p_prev, q_prev = cf_terms[0], 1
        p_curr, q_curr = cf_terms[0] * cf_terms[1] + 1, cf_terms[1]
    
        for i in range(2, len(cf_terms)):
                
                # Calculate mediants between p_prev/q_prev and p_curr/q_curr
                # The terms in the continued fraction can be large, e.g., 292.
                # This loop handles mediants efficiently.
                for m in range(1, cf_terms[i] + 1):
                        p_mediant = p_prev + m * p_curr
                        q_mediant = q_prev + m * q_curr
                
                        if q_mediant > b:
                                # Denominator exceeds the limit, stop and check the previous convergent
                                break
                                
                        if a <= q_mediant <= b:
                                error = abs(Fraction(p_mediant, q_mediant) - math.pi)
                                if error < min_error:
                                        min_error = error
                                        best_p, best_q = p_mediant, q_mediant
                
                # Update for the next convergent
                p_next = cf_terms[i] * p_curr + p_prev
                q_next = cf_terms[i] * q_curr + q_prev
                
                p_prev, q_prev = p_curr, q_curr
                p_curr, q_curr = p_next, q_next
                
                # If the next convergent's denominator is already too large, we can stop
                if q_curr > b:
                        break

        # If no fraction was found in the range, a brute-force check
        # of the first fraction greater than b might be needed.
        # The logic above ensures we have the best from convergents and mediants.
        return best_p, best_q

def test(tup:tuple) -> None:
        a,b = tup[0], tup[1]
        result_bf = best_fractions_bruteforce(a, b)
        print(f'The best brute force approximation of pi with denominator between {a} and {b} is {result_bf[1]}/{result_bf[0]}.')

        p, q = find_best_approximation(a, b)
        if p != -1 and q != -1:
                print(f"The best approximation of pi with denominator between {a} and {b} is {p}/{q}.")
                print(f"Decimal value: {p/q}")
                print(f"Error: {abs(p/q - math.pi)}")
        else:
                print(f"No suitable approximation found in the given range [{a}, {b}].")

if __name__ == '__main__':

        # Example usage
        test_cases = [(1,10), (100, 200), (100, 1000), (1000, 10000), (10000, 100000)]
        for case in test_cases:
                test(case)


