#import the linear solver wrapper
from ortools.linear_solver import pywraplp

def MIPProblem():
    #declare the MIP solver
    #문제에 대한 MIP solver를 선언하는 것.
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return

    #define the variables
    infinity = solver.infinity()
    #x and y are integer non-negative variables.
    x = solver.IntVar(0.0, infinity, 'x')
    y = solver.IntVar(0.0, infinity, 'y')

    print('Number of variables = ', solver.NumVariables())
    # non-negative 정수값을 가지는 x, y 변수를 생성시키기 위해 MakeIntVar 메소드를 사용함.

    #define the constraints
    #x + 7 * y <= 17.5
    solver.Add(x+7*y <= 17.5)
    #x <= 3.5
    solver.Add(x<=3.5)

    print('Number of constraints =', solver.NumConstraints())

    #define the objective
    #문제에 대한 objective function을 정의한다
    #Maximize x+10*y
    solver.Maximize(x+10*y)

    #call the solver
    status = solver.Solve()

    #display the solution
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value=', solver.Objective().Value())
        print('x = ', x.solution_value())
        print('y =', y.solution_value())
    else:
        print('The problem does not have an optimal solution.')

MIPProblem()