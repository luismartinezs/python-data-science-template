import numpy as np
import scipy.optimize as optimize
import matplotlib.pyplot as plt

# -- Configurable Parameters and Inputs --

# Space Dimensionality
N_DIMENSIONS = 2

# Potential Energy Function V(x)
# Takes an N-dimensional point (numpy array) and returns a scalar potential
# Example 1: Simple quadratic bowl centered at origin
# def potential_v(point):
#     return np.sum(point**2)

# Example 2: Rastrigin function (more complex, non-convex)
def potential_v(point):
     if point.shape[0] != N_DIMENSIONS:
          raise ValueError(f"Input point has dimension {point.shape[0]}, expected {N_DIMENSIONS}")
     # Center the function away from origin for better visualization if A or B is near 0
     offset_point = point - np.array([2.0] * N_DIMENSIONS)
     return 10 * N_DIMENSIONS + np.sum(offset_point**2 - 10 * np.cos(2 * np.pi * offset_point))

# Fixed Start and End Points (N_DIMENSIONS arrays)
POINT_A = np.array([-5.0] * N_DIMENSIONS)
POINT_B = np.array([5.0] * N_DIMENSIONS)

# Number of Intermediate Checkpoints
M_CHECKPOINTS = 20

# Distance Constraints
D_MIN = 0.5  # Minimum distance between ANY two distinct points in the full sequence (A, Q1..QM, B)
             # Also the minimum distance between consecutive points.
D_MAX = 2.0  # Maximum distance ONLY between CONSECUTIVE points in the sequence

# Optimization Parameters
MAX_ITERATIONS = 1000 # Max iterations for the optimizer
TOLERANCE = 1e-6     # Optimization tolerance

# Visualization
PLOT_RESULTS = True
PLOT_POTENTIAL_CONTOUR = True # Only works well for N_DIMENSIONS = 2

# -- End of Configuration --

# --- Helper Functions ---

def objective_function(q_flat, potential_func, n_dim):
    """
    Calculates the sum of potentials at the checkpoints.
    q_flat: Flat array of checkpoint coordinates (M * N_DIMENSIONS).
    potential_func: The potential function V.
    n_dim: Number of dimensions.
    """
    checkpoints = q_flat.reshape(-1, n_dim) # Reshape back to (M, N)
    total_potential = 0.0
    for q_i in checkpoints:
        total_potential += potential_func(q_i)
    return total_potential

def create_constraints(point_a, point_b, m, n_dim, d_min, d_max):
    """
    Creates the list of constraint dictionaries for scipy.optimize.minimize.
    """
    constraints = []
    num_points_total = m + 2 # Total points including A and B

    # --- Constraint Functions ---
    # These functions take the flat variable vector `q_flat` as input

    # Constraint: d_min <= ||P_i+1 - P_i|| <= d_max (consecutive)
    for i in range(num_points_total - 1):
        # Lower bound: ||P_i+1 - P_i|| - d_min >= 0
        def cons_min_consecutive(q_flat, i=i): # Use default arg capture for i
            checkpoints = q_flat.reshape(-1, n_dim)
            full_path = np.vstack([point_a, checkpoints, point_b])
            dist = np.linalg.norm(full_path[i+1] - full_path[i])
            return dist - d_min

        # Upper bound: d_max - ||P_i+1 - P_i|| >= 0
        def cons_max_consecutive(q_flat, i=i): # Use default arg capture for i
            checkpoints = q_flat.reshape(-1, n_dim)
            full_path = np.vstack([point_a, checkpoints, point_b])
            dist = np.linalg.norm(full_path[i+1] - full_path[i])
            return d_max - dist

        constraints.append({'type': 'ineq', 'fun': cons_min_consecutive})
        constraints.append({'type': 'ineq', 'fun': cons_max_consecutive})

    # Constraint: ||P_j - P_i|| >= d_min (non-consecutive)
    for i in range(num_points_total):
        for j in range(i + 2, num_points_total): # j starts from i+2 to ensure non-consecutive
             # Lower bound: ||P_j - P_i|| - d_min >= 0
            def cons_min_non_consecutive(q_flat, i=i, j=j): # Use default arg capture
                checkpoints = q_flat.reshape(-1, n_dim)
                full_path = np.vstack([point_a, checkpoints, point_b])
                dist = np.linalg.norm(full_path[j] - full_path[i])
                return dist - d_min

            constraints.append({'type': 'ineq', 'fun': cons_min_non_consecutive})

    return constraints

def generate_initial_guess(point_a, point_b, m, n_dim):
    """
    Generates a simple linear interpolation initial guess for the checkpoints.
    """
    initial_checkpoints = np.zeros((m, n_dim))
    for i in range(m):
        fraction = (i + 1.0) / (m + 1.0)
        initial_checkpoints[i] = point_a + fraction * (point_b - point_a)
    return initial_checkpoints.flatten() # Return as flat array

# --- Main Execution ---

if __name__ == "__main__":
    print("--- Problem Setup ---")
    print(f"Dimensions (N): {N_DIMENSIONS}")
    print(f"Start Point (A): {POINT_A}")
    print(f"End Point (B): {POINT_B}")
    print(f"Checkpoints (M): {M_CHECKPOINTS}")
    print(f"Min Distance (d_min): {D_MIN}")
    print(f"Max Consecutive Dist (d_max): {D_MAX}")
    print(f"Potential Function: {potential_v.__name__}")
    print("-" * 20)

    # Generate initial guess
    q_initial_flat = generate_initial_guess(POINT_A, POINT_B, M_CHECKPOINTS, N_DIMENSIONS)
    initial_checkpoints = q_initial_flat.reshape(-1, N_DIMENSIONS)
    initial_path = np.vstack([POINT_A, initial_checkpoints, POINT_B])

    print("Calculating Initial Objective...")
    initial_objective = objective_function(q_initial_flat, potential_v, N_DIMENSIONS)
    print(f"Initial Objective (Sum V(Qi)): {initial_objective:.4f}")

    # Create constraints
    print("Generating constraints...")
    constraints = create_constraints(POINT_A, POINT_B, M_CHECKPOINTS, N_DIMENSIONS, D_MIN, D_MAX)
    print(f"Generated {len(constraints)} constraints.")

    # Run the optimization
    print("Starting optimization (Method: SLSQP)...")
    result = optimize.minimize(
        fun=objective_function,
        x0=q_initial_flat,
        args=(potential_v, N_DIMENSIONS),
        method='SLSQP', # Sequential Least Squares Programming handles constraints
        constraints=constraints,
        options={'maxiter': MAX_ITERATIONS, 'ftol': TOLERANCE, 'disp': True} # Show optimizer output
    )
    print("-" * 20)

    # Process results
    if result.success:
        print("Optimization Successful!")
        q_optimal_flat = result.x
        optimal_checkpoints = q_optimal_flat.reshape(-1, N_DIMENSIONS)
        optimal_path = np.vstack([POINT_A, optimal_checkpoints, POINT_B])
        final_objective = result.fun

        print(f"Final Objective (Sum V(Qi)): {final_objective:.4f}")
        print("Optimal Checkpoints (Q1...QM):")
        print(optimal_checkpoints)

        # Verification of constraints (optional, for checking)
        print("\nVerifying final constraints (approximate):")
        valid = True
        for i in range(M_CHECKPOINTS + 1):
            dist = np.linalg.norm(optimal_path[i+1] - optimal_path[i])
            print(f"  ||P{i+1} - P{i}|| = {dist:.4f} (Allowed: [{D_MIN}, {D_MAX}])")
            if not (D_MIN - TOLERANCE <= dist <= D_MAX + TOLERANCE):
                 valid = False
                 print(f"    -> CONSECUTIVE DISTANCE VIOLATION for pair P{i}, P{i+1}")

        for i in range(M_CHECKPOINTS + 2):
            for j in range(i + 2, M_CHECKPOINTS + 2):
                 dist = np.linalg.norm(optimal_path[j] - optimal_path[i])
                 # print(f"  ||P{j} - P{i}|| = {dist:.4f} (Min Allowed: {D_MIN})") # Uncomment for verbose check
                 if dist < D_MIN - TOLERANCE:
                     valid = False
                     print(f"    -> NON-CONSECUTIVE DISTANCE VIOLATION for pair P{i}, P{j} (Dist: {dist:.4f})")
        if valid:
             print("All constraints appear satisfied within tolerance.")
        else:
             print("WARNING: Some constraints may be violated!")


    else:
        print("Optimization Failed!")
        print(f"Message: {result.message}")
        optimal_path = initial_path # Keep initial path if failed
        final_objective = initial_objective

    # --- Visualization (only for N_DIMENSIONS = 2) ---
    if PLOT_RESULTS and N_DIMENSIONS == 2:
        print("\nGenerating plot...")
        plt.figure(figsize=(10, 8))

        # Plot potential contour
        if PLOT_POTENTIAL_CONTOUR:
            x_range = np.linspace(min(POINT_A[0], POINT_B[0]) - 2, max(POINT_A[0], POINT_B[0]) + 2, 100)
            y_range = np.linspace(min(POINT_A[1], POINT_B[1]) - 2, max(POINT_A[1], POINT_B[1]) + 2, 100)
            X, Y = np.meshgrid(x_range, y_range)
            Z = np.zeros_like(X)
            for i in range(X.shape[0]):
                for j in range(X.shape[1]):
                    Z[i, j] = potential_v(np.array([X[i, j], Y[i, j]]))
            contour = plt.contourf(X, Y, Z, levels=50, cmap='viridis', alpha=0.7)
            plt.colorbar(contour, label='Potential V')

        # Plot paths
        plt.plot(initial_path[:, 0], initial_path[:, 1], 'o--', color='grey', alpha=0.6, label='Initial Path')
        plt.plot(optimal_path[:, 0], optimal_path[:, 1], 'o-', color='red', linewidth=2, label=f'Optimal Path (Obj: {final_objective:.2f})')

        # Plot A and B
        plt.plot(POINT_A[0], POINT_A[1], 's', color='blue', markersize=10, label='Start (A)')
        plt.plot(POINT_B[0], POINT_B[1], 's', color='green', markersize=10, label='End (B)')

        # Plot optimal checkpoints distinctly
        if result.success:
             optimal_q = optimal_path[1:-1,:]
             plt.plot(optimal_q[:, 0], optimal_q[:, 1], 'o', color='yellow', markersize=6, label='Optimal Q')


        plt.title(f'Optimal Path Finding ({potential_v.__name__})')
        plt.xlabel('Dimension 1')
        plt.ylabel('Dimension 2')
        plt.legend()
        plt.grid(True, linestyle=':', alpha=0.6)
        plt.axis('equal')
        plt.show()
    elif PLOT_RESULTS and N_DIMENSIONS != 2:
        print("\nPlotting is only enabled for N_DIMENSIONS = 2.")