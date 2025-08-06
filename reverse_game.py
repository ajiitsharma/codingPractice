#!/usr/bin/env python3 

'''
Akash and Akhil are playing a game. They have  balls numbered from  to . Akhil asks Akash to reverse the position of the balls, i.e., to 
change the order from say, 0,1,2,3 to 3,2,1,0. He further asks Akash to reverse the position of the balls  times, each time starting from one position 
further to the right, till he reaches the last ball. So, Akash has to reverse the positions of the ball starting from  position, then from  position,
then from  position and so on. At the end of the game, Akhil will ask Akash the final position of any ball numbered . 
Akash will win the game, if he can answer. Help Akash.

Write a function `reverse_game` that takes an integer `n` and returns the final position of the ball numbered `n` after performing the described operations.
'''

import math

def reverse_game(n, k):
    # Create a list of balls
    balls = list(range(n))
    
    # Perform the swapping operations n times. Each time swap the ith ball with the last ball
    for i in range(n):
        balls[i], balls[n-1] = balls[n-1], balls[i]
    
    # Return the final position of the ball numbered k
    return balls.index(k)+1

if __name__ == '__main__':
    # Test cases
    test_cases = [(5, 0), (10, 1), (3, 2), (3,1)]

    for n, k in test_cases:
        result = reverse_game(n, k)
        print(f"Final position of ball {k} in {n} balls: {result}")
