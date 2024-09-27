import random
import time
import matplotlib.pyplot as plt

def findParetoOptimalpoints(points):
    if len(points) <= 1:
        return points

    mid = len(points) // 2
    left_half = points[:mid]
    right_half = points[mid:]

    left_optimal = findParetoOptimalpoints(left_half)
    right_optimal = findParetoOptimalpoints(right_half)

    return merge(left_optimal, right_optimal)

def merge(left, right):
    merged = []
    max_y = float('-inf')

    left.sort(key=lambda p: (p[0], -p[1]))
    right.sort(key=lambda p: (p[0], -p[1]))

    for point in left + right:
        if point[1] > max_y:
            merged.append(point)
            max_y = point[1]

    return merged

n = 9000

points = [(random.randint(1, 9999), random.randint(1, 9999)) for _ in range(n)]

start_time = time.time()

pareto_points = findParetoOptimalpoints(points)

end_time = time.time()

# Time taken for execution of algorithm
print(end_time - start_time)

# The Pareto-Optimal points
print("\n The Pareto-optimal points are")
for point in pareto_points:
    print(point)


plt.figure(figsize=(10, 6))

x_all, y_all = zip(*points)
plt.scatter(x_all, y_all, color='blue', label='All Points', alpha=0.5)

x_pareto, y_pareto = zip(*pareto_points)
plt.scatter(x_pareto, y_pareto, color='red', label='Pareto Optimal Points', marker='o')

plt.title('Pareto Optimal Points Visualization')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.xlim(0, 10500)
plt.ylim(0, 10500)
plt.grid()
plt.show()
