import pytest
from src.levels import generate_problem, Problem

def test_problem_string_representation():
    problem = Problem(5, 3, '+', 8)
    assert str(problem) == "5 + 3 = ?"

def test_grade_1_problem():
    problem = generate_problem(1)
    assert problem.num1 <= 10
    assert problem.num2 <= 10
    assert problem.operator in ['+', '-']
    if problem.operator == '-':
        assert problem.num1 >= problem.num2  # No negative results

def test_grade_2_problem():
    problem = generate_problem(2)
    assert problem.num1 <= 20
    assert problem.num2 <= 20
    assert problem.operator in ['+', '-']
    if problem.operator == '-':
        assert problem.num1 >= problem.num2

def test_grade_3_problem():
    problem = generate_problem(3)
    assert problem.num1 <= 50
    assert problem.operator in ['+', '-', '*']
    if problem.operator == '*':
        assert problem.num2 <= 10
    else:
        assert problem.num2 <= 50
        if problem.operator == '-':
            assert problem.num1 >= problem.num2

def test_grade_4_problem():
    problem = generate_problem(4)
    assert problem.num1 <= 100
    assert problem.operator in ['+', '-', '*', '/']
    if problem.operator == '*':
        assert problem.num2 <= 12
    elif problem.operator == '/':
        assert problem.num2 <= 12
        assert problem.num1 % problem.num2 == 0  # Ensure clean division
    else:
        assert problem.num2 <= 100

def test_grade_5_problem():
    problem = generate_problem(5)
    assert problem.num1 <= 200
    assert problem.operator in ['+', '-', '*', '/']
    if problem.operator == '*':
        assert problem.num2 <= 15
    elif problem.operator == '/':
        assert problem.num2 <= 15
        assert problem.num1 % problem.num2 == 0
    else:
        assert problem.num2 <= 200

def test_problem_answers():
    for grade in range(1, 6):
        problem = generate_problem(grade)
        if problem.operator == '+':
            assert problem.answer == problem.num1 + problem.num2
        elif problem.operator == '-':
            assert problem.answer == problem.num1 - problem.num2
        elif problem.operator == '*':
            assert problem.answer == problem.num1 * problem.num2
        elif problem.operator == '/':
            assert problem.answer == problem.num1 // problem.num2