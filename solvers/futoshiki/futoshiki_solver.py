from ortools.sat.python import cp_model
from solvers.common.grid import Grid
from solvers.constraints.column_all_different import ColumnAllDifferent
from solvers.constraints.predefined_values import PredefinedValues
from solvers.constraints.row_all_different import RowAllDifferent


class FutoshikiSolver:
    def solve(self, grid_template: Grid) -> Grid:
        model = cp_model.CpModel()
        grid_length = grid_template.length
        solver_board = [
            [
                model.NewIntVar(1, grid_length, f"Cell({row},{col})")
                for col in range(grid_length)
            ]
            for row in range(grid_length)
        ]

        RowAllDifferent().apply(model, solver_board)
        ColumnAllDifferent().apply(model, solver_board)
        PredefinedValues(grid_template).apply(model, solver_board)

        for expr in grid_template.get_expressions():
            left_value = solver_board[expr.left.row][expr.left.column]
            right_value = solver_board[expr.right.row][expr.right.column]
            model.Add(expr.op.eval(left_value, right_value))

        solver = cp_model.CpSolver()
        status = solver.Solve(model)
        if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
            return self.__to_solved_grid(solver, solver_board)
        else:
            raise Exception(
                f"Killer Sudoku could not be solved. Status = {self.__status_to_message(status)}"
            )

    def __status_to_message(self, status) -> str:
        if status == cp_model.INFEASIBLE:
            return "INFEASIBLE"
        elif status == cp_model.MODEL_INVALID:
            return "MODEL_INVALD"
        else:
            return "UNKNOWN"

    def __to_solved_grid(self, solver, solved_board) -> Grid:
        grid_length = len(solved_board)
        grid = Grid(grid_length)
        for row_index in range(grid_length):
            for column_index in range(grid_length):
                solved_cell_value = solver.Value(solved_board[row_index][column_index])
                cell = grid.get_cell(row_index, column_index)
                cell.set_value(solved_cell_value)
        return grid