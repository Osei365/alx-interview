#!/usr/bin/python3
"""prime game"""


def isWinner(x, nums):
    """gets winner from prime game"""

    ben_wins = 0
    maria_wins = 0

    for i in range(x):
        n = nums[i]
        choice_list = [no for no in range(1, n + 1)]
        turn = 0
        while any([isprime(state) for state in choice_list]):
            for item in choice_list:  
                if isprime(item):
                    break
            mul = 1
            while item in choice_list:
                
                idx = choice_list.index(item)
                del choice_list[idx]
                mul += 1
                item = item * mul
            
            if turn == 0:
                turn = 1
            elif turn == 1:
                turn = 0
        if turn == 0:
            ben_wins += 1
        elif turn == 1:
            maria_wins += 1
    if ben_wins > maria_wins:
        return 'Ben'
    elif maria_wins > ben_wins:
        return 'Maria'

        

def isprime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5)+1):
        
        if num % i == 0:
            return False
    
    return True

if __name__ == "__main__":
    result = isWinner(3, [4, 5, 1])
    print(result)