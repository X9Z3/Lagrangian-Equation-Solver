def EquationScrubber(equation: str) -> tuple[str, bool]:
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