from solve import n_queens


def test_solution():
    assert n_queens(1) == 1
    assert n_queens(2) == 0
    assert n_queens(3) == 0
    assert n_queens(4) == 2
    assert n_queens(5) == 10
    assert n_queens(6) == 4
    assert n_queens(7) == 40
    assert n_queens(8) == 92
    assert n_queens(9) == 352
