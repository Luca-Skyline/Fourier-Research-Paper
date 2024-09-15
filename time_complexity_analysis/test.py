import random


def generate_floats(total, count):
    # Generate random float points
    points = sorted([random.uniform(0, total) for _ in range(count - 1)])

    # Compute the gaps between the points and total
    values = [points[0]] + [points[i + 1] - points[i] for i in range(count - 2)] + [total - points[-1]]

    return values


# Generate 4 random floats that sum up to 20
random_floats = generate_floats(20, 4)
print(random_floats)
print("Sum:", sum(random_floats))