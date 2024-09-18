from __future__ import annotations


from stacker.stacker import Stacker

import numpy as np


def _pow(x1, x2):
    return np.power(x1, x2).tolist()


def _log(x):
    return np.log(x).tolist()


def _log2(x):
    return np.log2(x).tolist()


def _log10(x):
    return np.log10(x).tolist()


def _exp(x):
    return np.exp(x).tolist()


def _sin(x):
    return np.sin(x).tolist()


def _cos(x):
    return np.cos(x).tolist()


def _tan(x):
    return np.tan(x).tolist()


def _asin(x):
    return np.arcsin(x).tolist()


def _acos(x):
    return np.arccos(x).tolist()


def _atan(x):
    return np.arctan(x).tolist()


def _sinh(x):
    return np.sinh(x).tolist()


def _cosh(x):
    return np.cosh(x).tolist()


def _tanh(x):
    return np.tanh(x).tolist()


def _asinh(x):
    return np.arcsinh(x).tolist()


def _acosh(x):
    return np.arccosh(x).tolist()


def _atanh(x):
    return np.arctanh(x).tolist()


def _sqrt(x):
    return np.sqrt(x).tolist()


def _gcd(x1, x2):
    return np.gcd(x1, x2).tolist()


def _lcm(x1, x2):
    return np.lcm(x1, x2).tolist()


def _radians(deg):
    return np.radians(deg).tolist()


def _ceil(x):
    return np.ceil(x).tolist()


def _floor(x):
    return np.floor(x).tolist()


def _abs(x):
    return np.abs(x).tolist()


def _cbrt(x):
    return np.cbrt(x).tolist()


math_operators = {
    "^": {
        "func": (lambda x1, x2: _pow(x1, x2)),
        "arg_count": 2,
        "push_result_to_stack": True,
        "desc": "Power",
    },
    "log": {
        "func": (lambda x: _log(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Logarithm",
    },
    "log2": {
        "func": (lambda x: _log2(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Logarithm base 2",
    },
    "log10": {
        "func": (lambda x: _log10(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Logarithm base 10",
    },
    "exp": {
        "func": (lambda x: _exp(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Exponential",
    },
    "sin": {
        "func": (lambda x: _sin(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Sine",
    },
    "cos": {
        "func": (lambda x: _cos(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Cosine",
    },
    "tan": {
        "func": (lambda x: _tan(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Tangent",
    },
    "asin": {
        "func": (lambda x: _asin(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Arcsine",
    },
    "acos": {
        "func": (lambda x: _acos(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Arccosine",
    },
    "atan": {
        "func": (lambda x: _atan(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Arctangent",
    },
    "sinh": {
        "func": (lambda x: _sinh(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Hyperbolic sine",
    },
    "cosh": {
        "func": (lambda x: _cosh(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Hyperbolic cosine",
    },
    "tanh": {
        "func": (lambda x: _tanh(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Hyperbolic tangent",
    },
    "asinh": {
        "func": (lambda x: _asinh(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Hyperbolic arcsine",
    },
    "acosh": {
        "func": (lambda x: _acosh(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Hyperbolic arccosine",
    },
    "atanh": {
        "func": (lambda x: _atanh(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Hyperbolic arctangent",
    },
    "sqrt": {
        "func": (lambda x: _sqrt(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Square root",
    },
    "gcd": {
        "func": (lambda x1, x2: _gcd(x1, x2)),
        "arg_count": 2,
        "push_result_to_stack": True,
        "desc": "Greatest common divisor",
    },
    "lcm": {
        "func": (lambda x1, x2: _lcm(x1, x2)),
        "arg_count": 2,
        "push_result_to_stack": True,
        "desc": "Least common multiple",
    },
    "radians": {
        "func": (lambda deg: _radians(deg)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Convert degrees to radians",
    },
    "ceil": {
        "func": (lambda x: _ceil(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Ceiling",
    },
    "floor": {
        "func": (lambda x: _floor(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Floor",
    },
    "abs": {
        "func": (lambda x: _abs(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Absolute value",
    },
    "cbrt": {
        "func": (lambda x: _cbrt(x)),
        "arg_count": 1,
        "push_result_to_stack": True,
        "desc": "Cube root",
    },
}

def setup(stacker: Stacker):
    for operator in math_operators:
        stacker.register_plugin(
            operator,
            math_operators[operator]["func"],
            # math_operators[operator]["arg_count"],
            push_result_to_stack=math_operators[operator]["push_result_to_stack"],
            desc=math_operators[operator]["desc"],
        )
