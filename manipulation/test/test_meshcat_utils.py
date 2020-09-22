import manipulation.meshcat_utils as dut

import numpy as np
from meshcat import Visualizer
from pydrake.all import MathematicalProgram, Solve

prog = MathematicalProgram()
x = prog.NewContinuousVariables(2)
prog.AddCost(x.dot(x))
prog.AddBoundingBoxConstraint(-2, 2, x)
result = Solve(prog)

meshcat = Visualizer()
X, Y = np.meshgrid(np.linspace(-3, 3, 35), np.linspace(-3, 3, 31))
dut.plot_mathematical_program(meshcat, prog, X, Y, result)