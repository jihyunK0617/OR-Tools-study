from ortools.sat.python import cp_model

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0
    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s = %i' % (v, self.Value(v)), end=' ')
        print()
    def solution_count(self):
        return self.__solution_count

def CPSAT():
    # Declare the model
    model = cp_model.CpModel()

    # Create the variables
    num_vals = 3
    x = model.NewIntVar(0, num_vals -1, 'x')
    y = model.NewIntVar(0, num_vals -1, 'y')
    z = model.NewIntVar(0, num_vals -1, 'z')
    # solver는 3개의 변수를 생성하는데 이들은 각각 0, 1 또는 2를 가질 수 있다

    # Create the constraint
    # constraint : x != y
    model.Add(x != y)

    all_solution = True
    solver = cp_model.CpSolver()
    if all_solution == False:
        # Call the solver
        status = solver.Solve(model)
        if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
            print('x = %i' % solver.Value(x))
            print('y = %i' % solver.Value(y))
            print('z = %i' % solver.Value(z))
        else:
            print('No solution found.')
    else:
        solution_printer = VarArraySolutionPrinter([x, y, z])
        solver.parameters.enumerate_all_solutions = True
        status = solver.Solve(model, solution_printer)
        print('Status = %s' % solver.StatusName(status))
        print('Number of solutions found: %i' % solution_printer.solution_count())

    # Display the first solution


CPSAT()
