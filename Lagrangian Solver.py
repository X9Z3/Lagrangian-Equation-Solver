import sympy as smp

"""
Semi-automated Equations of Motion calculator.

This script sets up symbolic variables for a double pendulum or similar system
using Lagrangian mechanics. It defines generalized coordinates, their time
derivatives, and computes Cartesian positions of the masses in terms of angular coordinates.
"""

# Define symbols
t = smp.Symbol('t', real=True)

# Generalized coordinates as functions of time
theta1, theta2 = smp.symbols('mass_1.angle mass_2.angle', cls=smp.Function, real=True)
theta1 = theta1(t)
theta2 = theta2(t)

# System parameters
l1, l2 = smp.symbols('mass_1.rod_length mass_2.rod_length', real=True, positive=True)
m1, m2 = smp.symbols('mass_1.mass mass_2.mass', real=True, positive=True)
g = smp.Symbol('gravity', real=True)

# Cartesian positions of the masses
x1 = l1 * smp.cos(theta1)
y1 = l1 * smp.sin(theta1)
x2 = x1 + l2 * smp.cos(theta2)
y2 = y1 + l2 * smp.sin(theta2)

# First-order derivatives (velocities)
dtheta1 = smp.diff(theta1, t)
dtheta2 = smp.diff(theta2, t)
dx1 = smp.diff(x1, t)
dy1 = smp.diff(y1, t)
dx2 = smp.diff(x2, t)
dy2 = smp.diff(y2, t)

# Second-order derivatives (accelerations)
ddtheta1 = smp.diff(dtheta1, t)
ddtheta2 = smp.diff(dtheta2, t)
ddx1 = smp.diff(dx1, t)
ddy1 = smp.diff(dy1, t)
ddx2 = smp.diff(dx2, t)
ddy2 = smp.diff(dy2, t)

def scrub(equation: str) -> tuple[str, bool]:
    """
    Transforms a symbolic equation string into a simplified format suitable for use
    in other programs. Specifically:
    - Replaces SymPy-style derivatives like 'Derivative(theta1(t), t)' with 'dtheta1'.
    - Removes function call notation like '(t)'.
    - Replaces certain variable patterns (e.g., 'dmass_1.angle') with project-specific equivalents.

    Args:
        equation (str): The equation string to be cleaned.

    Returns:
        tuple[str, bool]: A tuple containing:
            - The cleaned-up equation string.
            - A boolean indicating if parentheses are balanced.
    """
    # Remove SymPy-specific syntax
    cleaned = equation.replace('Derivative(', 'd')
    cleaned = cleaned.replace(', t)', '')
    cleaned = cleaned.replace('(t)', '')

    # Replace project-specific variable names
    cleaned = cleaned.replace('dmass_1.angle', 'mass_1.angular_velocity')
    cleaned = cleaned.replace('dmass_2.angle', 'mass_2.angular_velocity')

    # Check for balanced parentheses
    left_parens = cleaned.count('(')
    right_parens = cleaned.count(')')

    real_equation = left_parens == right_parens
    return cleaned, real_equation



# --- Energy Definitions ---

# Kinetic energy: T = 1/2 m v^2 for both masses
kinetic_energy = (
    smp.Rational(1, 2) * m1 * (dx1**2 + dy1**2) +
    smp.Rational(1, 2) * m2 * (dx2**2 + dy2**2)
)

# Potential energy: V = m g y for both masses
potential_energy = m1 * g * y1 + m2 * g * y2

# Lagrangian: L = T - V
lagrangian = kinetic_energy - potential_energy

# --- Equations of Motion using Euler-Lagrange ---

# d/dt (∂L/∂dθ) - ∂L/∂θ for each generalized coordinate
lagrangian_eqn_1 = smp.simplify(
    smp.diff(lagrangian, theta1) - smp.diff(smp.diff(lagrangian, dtheta1), t)
)
lagrangian_eqn_2 = smp.simplify(
    smp.diff(lagrangian, theta2) - smp.diff(smp.diff(lagrangian, dtheta2), t)
)

# Display the symbolic results and their string lengths
print(f"\nLagrangian Equation 1 (length {len(str(lagrangian_eqn_1))}):\n{lagrangian_eqn_1}")
print(f"\nLagrangian Equation 2 (length {len(str(lagrangian_eqn_2))}):\n{lagrangian_eqn_2}")

# --- Solve for Angular Accelerations ---

"""
NOTE:
Your second-order equations will contain ddtheta1 and ddtheta2.
Solve both equations simultaneously and choose the cleanest result for each variable.
"""

solved_equations = smp.solve(
    [lagrangian_eqn_1, lagrangian_eqn_2],
    [ddtheta1, ddtheta2],
    simplify=False, rational=False
)

# Apply simplification and trig simplification, lots of compute is spent here and further hand simp. can be done.
DDtheta1 = smp.trigsimp(smp.simplify(solved_equations[ddtheta1]))
DDtheta2 = smp.trigsimp(smp.simplify(solved_equations[ddtheta2]))

# Output final results after scrub
print("\nDDtheta1 (length {}):\n{}".format(len(str(DDtheta1)), scrub(str(DDtheta1))))
print("\nDDtheta2 (length {}):\n{}".format(len(str(DDtheta2)), scrub(str(DDtheta2))))
