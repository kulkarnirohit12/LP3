import matplotlib.pyplot as plt

# Function and its derivative
def f(x): 
    return (x + 3)**2

def df(x): 
    return 2*(x + 3)

# Parameters
x = 2
learning_rate = 0.01
precision = 0.00001
previous_step_size = 1
max_iters = 1000
iters = 0

# Gradient Descent loop
while previous_step_size > precision and iters < max_iters:
    prev_x = x
    x = x - learning_rate * df(prev_x)
    previous_step_size = abs(x - prev_x)
    iters += 1

print(f"Local minimum occurs at x = {x:.4f}")
print(f"f(x) = {f(x):.4f}")

# Plot
import numpy as np
X = np.linspace(-6, 2, 100)
Y = f(X)
plt.plot(X, Y, label="y = (x+3)^2")
plt.scatter(x, f(x), color='red', label='Local Minimum')
plt.legend()
plt.show()
