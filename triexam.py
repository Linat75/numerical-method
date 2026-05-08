import numpy as np

# --- Example data (monthly temp) ---
# x = months (1 to 12)
x = np.arange(1, 13)

# sample seasonal temperature data
y = np.array([29, 31, 34, 38, 40, 39, 36, 34, 33, 31, 30, 28])

# --- Design matrix ---
X = np.column_stack([
    np.ones_like(x),   # a0
    np.cos(x),         # a1
    np.sin(x)          # b1
])

# --- Least squares ---
coeffs, _, _, _ = np.linalg.lstsq(X, y, rcond=None)

a0, a1, b1 = coeffs

# --- Predicted values ---
y_fit = a0 + a1*np.cos(x) + b1*np.sin(x)

# --- R^2 calculation ---
ss_res = np.sum((y - y_fit)**2)
ss_tot = np.sum((y - np.mean(y))**2)
r2 = 1 - (ss_res / ss_tot)

# --- Amplitude ---
amplitude = np.sqrt(a1**2 + b1**2)

# --- Phase shift (month of peak) ---
phase = np.arctan2(-b1, a1)
peak_month = (phase * 12 / (2*np.pi)) % 12

# --- Output ---
print(f"a0 (mean temp) = {a0:.2f}")
print(f"a1 = {a1:.2f}")
print(f"b1 = {b1:.2f}")
print(f"Amplitude = {amplitude:.2f} °C")
print(f"R² = {r2:.4f}")
print(f"Phase shift ≈ peak month = {peak_month:.2f}")
