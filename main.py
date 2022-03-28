from yakuso.yakuso_solver import YakusoSolver

yakuso_solver = YakusoSolver()
solved = yakuso_solver.solve(
    [
        ["", "", "", "1", "", ""],
        ["", "", "", "", "3", ""],
        ["", "0", "", "4", "0", ""],
        ["", "", "", "", "", ""],
        ["5", "5", "", "", "", ""]
    ]
    ,["", "", "4", "12", "10", "9"], 5, 6)
print(solved)