#!/usr/bin/env python3

from simplex import Simplex
from fractions import Fraction

def test_case(num_vars, constraints, objective_function, expected_solution):
    s = Simplex(num_vars, constraints, objective_function)
    if expected_solution != s.solution:
        print("[FAIL] Expected '%' received '%'", expected_solution, s.solution)
    else:
        print("[OK] num_vars=", num_vars, " constraints='", constraints, "' objective='", objective_function, "' solution='", expected_solution ,"'")

test_case(2, ['2x_1 + 3x_2 <= 16', '3x_1 + 4x_2 <= 24', '1x_2 <= 5/2'], ("max", "4x_1 + 16x_2 "), {"x_1": Fraction(17, 4), "x_2": Fraction(5, 2)})
