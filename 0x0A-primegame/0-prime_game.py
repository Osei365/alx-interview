#!/usr/bin/python3
"""prime game"""


def isWinner(x, nums):
    """gets winner from prime game"""
    if not nums or x < 1:
        return None
    ben_wins = 0
    maria_wins = 0
    for i in range(x):
        n = nums[i]
        if n > 0:
            choice_list = [no for no in range(1, n + 1)]
        else:
            choice_list = [0]
        turn = 0
        while any([isprime(state) for state in choice_list]):
            for item in choice_list:
                if isprime(item):
                    break
            mul = 1
            init_item = item
            while item in choice_list:
                idx = choice_list.index(item)
                del choice_list[idx]
                mul += 1
                item = init_item * mul
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
    else:
        return None


def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
