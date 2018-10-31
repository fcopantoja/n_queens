from itertools import permutations
from db import session, Solution


def n_queens(n):
    count = 0
    cols = range(n)
    for permutation in permutations(cols):
        if n == len(set(permutation[i] + i for i in cols)) == len(set(permutation[i] - i for i in cols)):
            session.add(Solution(positions=permutation, number_of_queens=n))
            count += 1
    session.commit()
    print(f'Number of solution for {n} queens is {count}')
    return count


if __name__ == '__main__':
    print(n_queens(8))
