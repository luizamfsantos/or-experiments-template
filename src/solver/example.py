"""Minimal Pyomo model solved via Gurobi, as a template for the real solver core."""

from __future__ import annotations

import pyomo.environ as pyo


def build_example_model() -> pyo.ConcreteModel:
    model = pyo.ConcreteModel()
    model.x = pyo.Var(within=pyo.NonNegativeReals)
    model.y = pyo.Var(within=pyo.NonNegativeReals)
    model.capacity = pyo.Constraint(expr=model.x + model.y <= 10)
    model.objective = pyo.Objective(expr=2 * model.x + 3 * model.y, sense=pyo.maximize)
    return model


def solve_example(model: pyo.ConcreteModel | None = None) -> pyo.SolverResults:
    """Solve `model` (or a fresh example model) with Gurobi via Pyomo's solver interface."""
    model = model if model is not None else build_example_model()
    solver = pyo.SolverFactory("gurobi")
    return solver.solve(model)
