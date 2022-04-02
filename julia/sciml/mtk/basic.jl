using ModelingToolkit

@variables t x(t)  # independent and dependent variables
@parameters τ       # parameters
D = Differential(t) # define an operator for the differentiation w.r.t. time

@named fol_model = ODESystem(D(x) ~ (1 - x)/τ)

using DifferentialEquations
using Plots

prob = ODEProblem(fol_model, [x => 0.0], (0.0,10.0), [τ => 3.0])
plot(solve(prob))