from doplo.doplo_solver import DoploSolver
from suguru.suguru_solver import SuguruSolver

doplo_solver = DoploSolver()
solved = doplo_solver.solve(
    sum_rows=[
        3,
        6,
        1,
        0,
        3
    ],
    sum_cols=[
        5,
        4,
        0,
        6,
        0
    ],
    length=5
)
