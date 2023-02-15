from ortools.linear_solver import pywraplp

def create_data_model():
    data = {}
    data['constraint_coeffs'] = [
        [5, 7, 9, 2, 1],
        [18, 4, -9, 10, 12],
        [4, 7, 3, 8, 5],
        [5, 13, 16, 3, -7],
    ]
    data['bounds'] = [250, 285, 211, 315]
    data['obj_coeffs'] = [7, 8, 2, 9, 6]
    data['num_vars'] = 5
    data['num_constraints'] = 4
    return data

def usingArray():
    data = create_data_model()
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return
    infinity = solver.infinity()
    x = {}
    for j in range(data['num_vars']):
        x[j] = solver.IntVar(0, infinity, 'x[%i]' % j)
    print('Number of variables =', solver.NumVariables())

    #define the constraints
    for i in range(data['num_constraints']):
        #RowConstraint : 첫번째와 두번째 arg는 constraint의 lower, upper을 의미하며 세번째 arg는 constraint의 이름으로 옵션사항이다.
        constraint = solver.RowConstraint(0, data['bounds'][i], '')
        for j in range(data['num_vars']):
            #SetCoefficient : 이 메소드를 통해 변수의 계수를 정의한다.
            constraint.SetCoefficient(x[j], data['constraint_coeffs'][i][j])
    print('Number of constraints = ', solver.NumConstraints())

    #define the objective
    objective = solver.Objective()
    for j in range(data['num_vars']):
        objective.SetCoefficient(x[j], data['obj_coeffs'][j])
    objective.SetMaximization()

    #call the solver
    status = solver.Solve()

    # display the solution
    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value =', solver.Objective().Value())
        for j in range(data['num_vars']):
            print(x[j].name(), ' = ', x[j].solution_value())
        print()
        print('Problem solved in %f milliseconds' % solver.wall_time())
        print('Problem solved in %d iterations' % solver.iterations())
        print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
    else:
        print('The problem does not have an optimal solution.')

usingArray()
