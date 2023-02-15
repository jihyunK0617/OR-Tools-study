from ortools.sat.python import cp_model

model = cp_model.CpModel()

var_upper_bound = max(50, 45, 37)
x = model.NewIntVar(0, var_upper_bound, 'x')
y = model.NewIntVar(0, var_upper_bound, 'y')
z = model