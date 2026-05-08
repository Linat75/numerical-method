import numpy as np

# --- Data ---
x = np.array([1, 2, 3, 4, 5])
y = np.array([7.0, 3.7, 0.8, 0.23, 0.17])

# --- Linearization ---
Y = np.log(y)

# Fit line
b, A = np.polyfit(x, Y, 1)
a = np.exp(A)

# Correlation coefficient (THIS WAS MISSING)
r = np.corrcoef(x, Y)[0, 1]

print(f'Linearized: a={a:.4f}, b={b:.4f}, r={r:.4f}')
