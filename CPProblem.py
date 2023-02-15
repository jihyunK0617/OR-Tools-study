from ortools.sat.python import cp_model

model = cp_model.CpModel()

var_upper_bound = max(50, 45, 37)
x = model.NewIntVar(0, var_upper_bound, 'x')
y = model.NewIntVar(0, var_upper_bound, 'y')
z = model.NewIntVar(0, var_upper_bound, 'z')

# Define the constraints
# 계수가 정수가 아니므로 2를 곱해줌
model.Add(2*x + 7*y + 3*z <= 50)
model.Add(3*x -5*y +7*z <= 45)
model.Add(5*x + 2*y - 6*z <= 37)

model.Maximize(2*x + 2*y + 3*z)

# Call the solver
solver = cp_model.CpSolver()
status = solver.Solve(model)

#
