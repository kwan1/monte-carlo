import matplotlib.pyplot as plt
import random

def monte_carlo_pi(num_samples):
    inside_circle = 0

    # Lists to store coordinates for plotting
    inside_x, inside_y = [], []
    outside_x, outside_y = [], []

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = x**2 + y**2

        if distance <= 1:
            inside_circle += 1
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)

    estimated_pi = (inside_circle / num_samples) * 4
    return estimated_pi, inside_x, inside_y, outside_x, outside_y

def plot_points(inside_x, inside_y, outside_x, outside_y):
    plt.scatter(inside_x, inside_y, color='blue', marker='.')
    plt.scatter(outside_x, outside_y, color='red', marker='.')
    plt.title("Monte Carlo Estimation of π")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

# Number of random samples
num_samples = int(input("Enter the number of samples: "))

# Estimate π using Monte Carlo
result, inside_x, inside_y, outside_x, outside_y = monte_carlo_pi(num_samples)

# Print the result
print(f"Estimated value of π using {num_samples} samples: {result}")

# Plot points for visualization
plot_points(inside_x, inside_y, outside_x, outside_y)

