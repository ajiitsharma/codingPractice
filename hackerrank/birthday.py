import math
import random
from collections import Counter

def simulate_birthday(n: int, k: int) -> float:
    """
    Simulate the birthday problem to estimate the probability that at atleast k people in a group of n share the same birthday.

    :param n: Number of people in the group
    :param k: Number of simulations to run
    :return: Estimated probability that at least k people share a birthday
    """
    if n <= 0:
        return 0.0
    if n > 365:
        return 1.0  # Pigeonhole principle

    NSimulations = 100000

    successful_trials = 0

    for _ in range(NSimulations):
        birthdays = [random.randint(1, 365) for _ in range(n)]

        # Count the frequency of each birthday
        birthday_counts = Counter(birthdays)
        
        # Check if any birthday has a count of k.
        if k > 1: 
            # Check if any birthday has a count of k or more.
            # This is the "at least k" condition.
            if any(count >= k for count in birthday_counts.values()):
                successful_trials += 1


    return successful_trials / NSimulations

def combination(n: int, k: int) -> int:
    """
    Calculate the number of combinations of n items taken k at a time.
    
    :param n: Total number of items
    :param k: Number of items to choose
    :return: Number of combinations
    """
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    
    numerator = math.factorial(n)
    denominator = math.factorial(k) * math.factorial(n - k)
    
    return numerator // denominator


def probability_of_k_common_birthday(n: int, k: int) -> float:
    """
    Calculate the probability that exactly n people in a group share the same birthday.
    
    :param n: Number of people in the group
    :return: Probability that exactly n people share a birthday
    """
    if n <= 0:
        return 0.0
    if n > 365:
        return 0.0  # More people than days, impossible to have exactly n sharing a birthday
    
    # Using the formula for the probability of exactly n people sharing a birthday
    probability = 365 * combination(n, k) * (1 / 365) ** k

    for i in range(n - k):
        probability *= (364 - i) / 365
    
    return probability

def probability_of_common_birthday(n: int) -> float:
    """
    Calculate the probability that at least two people in a group of n people share the same birthday.
    
    :param n: Number of people in the group
    :return: Probability that at least two people share a birthday
    """
    if n <= 0:
        return 0.0
    if n > 365:
        return 1.0  # Pigeonhole principle
    
    probability_unique = 1.0
    for i in range(n):
        probability_unique *= (365 - i) / 365
    
    return 1 - probability_unique

if __name__ == '__main__':
    # Test cases
    test_cases = [5, 10, 20, 22, 24, 26, 28, 30, 40, 50, 60, 70, 80, 90, 100]

    for n in test_cases:
        result = probability_of_common_birthday(n)
        print(f"Prob(X > 2, N= {n}): {result*100:.2f}%")
        result = probability_of_k_common_birthday(n, 2)
        print(f"Prob(X = 2, N= {n}): {result*100:.2f}%")
        result = simulate_birthday(n, 2)
        print(f"Simulated Prob(X = 2, N= {n}): {result*100:.2f}%")
        print("-" * 50)
