from typing import List
from ortools.sat.python import cp_model
from itertools import product


class YakusoSolver:
    def solve(
        self, template: List[List[str]], sums: List[str], rows: int, cols: int
    ) -> List[List[int]]:
        model = cp_model.CpModel()
        board = [
            [model.NewIntVar(0, rows, f"({_i},{_j})") for _j in range(cols)]
            for _i in range(rows)
        ]
        for i in range(rows):
            for j in range(cols):
                if len(template[i][j]) > 0:  # elements are strings, so check for length
                    model.Add(
                        board[i][j] == int(template[i][j])
                    )  # and cast back to int
        # Sum over all rows for column is equal to predefined value
        for j in range(len(sums)):
            if len(sums[j]) > 0:
                total = 0
                for i in range(rows):
                    total += board[i][j]
                model.Add(total == int(sums[j]))
        solver = cp_model.CpSolver()
        status = solver.Solve(model)
        if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
            for i in range(rows):
                for j in range(cols):
                    print(f"[{solver.Value(board[i][j])}] ", end="")
                print("\n")
        return None
