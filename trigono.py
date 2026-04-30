import numpy as np

# --- Model: y = a*sin(x) + b*cos(x) ---
def trig_fit(x, y):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)

    # Design matrix
    A = np.column_stack((np.sin(x), np.cos(x)))

    # Solve least squares
    coeff, _, _, _ = np.linalg.lstsq(A, y, rcond=None)

    a, b = coeff
    return a, b

# --- Example Data ---
x = [0, 1, 2, 3, 4, 5]
y = [0.1, 0.9, 0.5, -0.4, -0.8, -0.1]

# --- Run ---
a, b = trig_fit(x, y)

print("Trigonometric Fit Result:")
print("a =", a)
print("b =", b)
print("Model: y = a*sin(x) + b*cos(x)")
