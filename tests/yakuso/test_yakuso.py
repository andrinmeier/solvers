from yakuso.yakuso_solver import YakusoSolver


def get_template():
    return [
        ["", "", "", "1", "", ""],
        ["", "", "", "", "3", ""],
        ["", "0", "", "4", "0", ""],
        ["", "", "", "", "", ""],
        ["5", "5", "", "", "", ""],
    ]

def get_sum_columns():
    return ["", "", "4", "12", "10", "9"]

def test_preinitializes_board_correctly():
    yakuso_solver = YakusoSolver()
    rows = 5
    cols = 6
    template = get_template()
    sum_cols = get_sum_columns()
    solved = yakuso_solver.solve(template, sum_cols, rows, cols)
    for i in range(rows):
        for j in range(cols):
            if len(template[i][j]) > 0:
                assert solved[i][j] == int(template[i][j])

def test_cols_sum_correctly():
    yakuso_solver = YakusoSolver()
    rows = 5
    cols = 6
    template = get_template()
    sum_cols = get_sum_columns()
    solved = yakuso_solver.solve(template, sum_cols, rows, cols)
    for j in range(cols):
        total = 0
        for i in range(rows):
            total += solved[i][j]
        if len(sum_cols[j]) > 0:
            assert total == int(sum_cols[j])
