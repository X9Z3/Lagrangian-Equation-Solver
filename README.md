# EOM Generator

A lightweight, symbolic mechanics utility for automatically generating the equations of motion (EOM) for physical systems using Lagrangian mechanics with [SymPy](https://www.sympy.org/en/index.html).

This tool is designed to be reusable and modular, allowing it to serve as a backend module for simulation projects—such as a [double pendulum](https://github.com/your-username/double-pendulum)—by providing analytically derived second-order differential equations from symbolic energy expressions.

---

## 🧠 What It Does

- Defines system dynamics using symbolic variables.
- Computes kinetic and potential energy.
- Derives the Lagrangian.
- Applies the Euler–Lagrange equations.
- Solves for angular accelerations (`ddtheta1`, `ddtheta2`) symbolically.
- Exports simplified expressions, scrubbed of SymPy-specific syntax for use in other languages or programs.


Future work looks to include full equation automation and overhauling as a class for ease of use elsewhere.
