from itertools import permutations
from db import session, Solution


def n_queens(n):
    count = 0
    columns = range(n)
    for permutation in permutations(columns):
        if n == len(set(permutation[i] + i for i in columns)) == len(set(permutation[i] - i for i in columns)):
            session.add(Solution(positions=permutation, number_of_queens=n))
            count += 1

        if count:
            session.commit()

    print(f'Number of solution for {n} queens is {count}')
    return count


if __name__ == '__main__':
    print(n_queens(8))
