# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# import the required libraries.
from ortools.linear_solver import pywraplp
from ortools.init import pywrapinit

def test():
    # declare the solver
     # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return


    # create the variables.
     # create the variables x and y.
    x = solver.NumVar(0,1,'x')
    y = solver.NumVar(0,2,'y')

    print('Number of variables = ', solver.NumVariables())

    # define constraints.
     # create a linear constraints
    ct = solver.Constraint(0, 2, 'ct') # 0 <= x + y <= 2
    ct.SetCoefficient(x, 1) # 0 <= x <= 1
    ct.SetCoefficient(y, 1) # 0 <= y <= 2
    print('Number of constraints =', solver.NumConstraints()) # NumConstraints sets the coefficients of x and y in expression for constraint.

    # define the objective function
     # create the objective function, 3 * x + y
    objective = solver.Objective()
    objective.SetCoefficient(x, 3)
    objective.SetCoefficient(y, 1)
    objective.SetMaximization() # SetMaximization declares this to be a maximization problem.

    # invoke the solver and display the results.
    solver.Solve()
    print('Solution:')
    print('Objective value = ', objective.Value())
    print('x = ', x.solution_value())
    print('y = ', y.solution_value())


test()
# if __name__ == '__main__':
#     pywrapinit.CppBridge.InitLogging('basic_example.py')
#     cpp_flags = pywrapinit.CppFlags()
#     cpp_flags.logtostderr = True
#     cpp_flags.log_prefix = False
#     pywrapinit.CppBridge.SetFlags(cpp_flags)
#
#     test()
