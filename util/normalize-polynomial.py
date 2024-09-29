# might not be perfect but kind of works


def normalize_polynomial(ranges, coefficients, exponents):
    # Validate input lengths
    if not (len(ranges) == len(coefficients) == len(exponents)):
        raise ValueError(
            "The lengths of ranges, coefficients, and exponents must be equal."
        )

    n = len(coefficients)
    total_coeff_sum = sum(coefficients)
    normalized_coeffs = []

    # Compute normalized coefficients
    for i in range(n):
        x_min, x_max = ranges[i]
        # Validate ranges
        if x_min >= x_max:
            raise ValueError(
                f"Invalid range for x_{i+1}: ({x_min}, {x_max}). x_min must be less than x_max."
            )

        a_i = coefficients[i]
        n_i = exponents[i]
        C_i = a_i / total_coeff_sum  # Desired contribution
        x_max_power = x_max**n_i
        a_i_norm = C_i / x_max_power
        normalized_coeffs.append(a_i_norm)

    # Print original polynomial
    print("Original Polynomial:")
    print_polynomial(coefficients, exponents)

    # Print normalized polynomial
    print("\nNormalized Polynomial:")
    print_polynomial(normalized_coeffs, exponents)

    # Return normalized coefficients and exponents
    return normalized_coeffs, exponents


def print_polynomial(coefficients, exponents):
    terms = []
    for i, (a_i, n_i) in enumerate(zip(coefficients, exponents), 1):
        term = term_to_string(a_i, f"x_{i}", n_i)
        if term:
            terms.append(term)
    polynomial = " + ".join(terms)
    print(f"G(x) = {polynomial}")


def term_to_string(coefficient, variable, exponent):
    # Skip zero coefficients
    if coefficient == 0:
        return ""
    # Format coefficient
    coeff_str = f"{coefficient:.6g}"  # Adjust precision as needed
    # Format variable and exponent
    if exponent == 0:
        return f"{coeff_str}"
    elif exponent == 1:
        return f"{coeff_str}{variable}"
    else:
        return f"{coeff_str}{variable}^{exponent}"


# Example usage:
if __name__ == "__main__":
    # Input
    ranges = [(1000, 10000), (0, 1), (10, 200)]
    coefficients = [0.8, 1, 1.7]
    exponents = [1.5, 0.8, 1]

    # Perform normalization
    try:
        normalized_coeffs, normalized_exponents = normalize_polynomial(
            ranges, coefficients, exponents
        )
    except ValueError as e:
        print(f"Error: {e}")

    mid_values = [5000, 0.5, 90]
    min_values = [1000, 0, 10]
    max_values = [10000, 1, 200]
    values = [5000, 0, 200]
    factors = [
        (value - range[0]) / (range[1] - range[0])
        for value, range in zip(values, ranges)
    ]
    print(f"Factors: {factors}")
