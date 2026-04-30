import numpy as np

# --- Exponential model ---
def exp_func(x, a, b):
    return a * np.exp(b * x)

# --- Fitting function (NO matplotlib, NO scipy) ---
def exponential_fit(x, y):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)

    results = {}

    # Method 1: Linearization
    Y = np.log(y)
    b, A = np.polyfit(x, Y, 1)
    a = np.exp(A)
    results["linear"] = (a, b)

    return results

# --- Data ---
x = [1, 2, 3, 4, 5]
y = [7.0, 3.7, 0.8, 0.23, 0.17]

# --- Run ---
results = exponential_fit(x, y)

print("Fitted parameters (a, b):")
print(results)
