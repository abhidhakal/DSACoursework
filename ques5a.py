#Implement travelling a salesman problem using hill climbing algorithm.

import random
import math

# Function to calculate the distance between two cities
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Function to calculate the total distance of the tour
def calculate_total_distance(route, locations):
    total = 0
    for i in range(len(route)):
        total += calculate_distance(locations[route[i]], locations[route[(i + 1) % len(route)]])
    return total

# Function to generate an initial solution
def create_initial_solution(locations):
    route = list(range(len(locations)))
    random.shuffle(route)
    return route

# Function to generate neighbors by swapping two cities
def create_neighbors(route):
    neighbors = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            neighbor = route[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

# Hill Climbing algorithm
def hill_climbing_algorithm(locations):
    current_route = create_initial_solution(locations)
    current_distance = calculate_total_distance(current_route, locations)
    while True:
        neighbors = create_neighbors(current_route)
        best_neighbor = None
        best_distance = current_distance
        for neighbor in neighbors:
            neighbor_distance = calculate_total_distance(neighbor, locations)
            if neighbor_distance < best_distance:
                best_neighbor = neighbor
                best_distance = neighbor_distance
        if best_neighbor is None:
            break
        current_route = best_neighbor
        current_distance = best_distance
    return current_route, current_distance

locations = [
    (0, 0), (1, 3), (4, 3), (6, 1),
    (3, 0), (2, 4), (5, 5), (7, 2)
]

# Solve TSP using Hill Climbing
optimal_route, minimal_distance = hill_climbing_algorithm(locations)
print("Best tour:", optimal_route)
print("Total distance:", minimal_distance)
