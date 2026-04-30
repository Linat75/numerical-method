import numpy as np

# --- Data (radioactive decay) ---
x = np.array([1, 2, 3, 4, 5])
y = np.array([7.0, 3.7, 0.8, 0.23, 0.17])

# --- Method 1: Linearization ---
Y = np.log(y)
b, A = np.polyfit(x, Y, deg=1)
a = np.exp(A)

print(f'Linearized: a={a:.4f}, b={b:.4f}')

# --- Method 2: "SciPy replacement" (same math idea) ---
# ln(y) = ln(a) + b x
b2, A2 = np.polyfit(x, np.log(y), 1)
a2 = np.exp(A2)

print(f'SciPy:      a={a2:.4f}, b={b2:.4f}')
