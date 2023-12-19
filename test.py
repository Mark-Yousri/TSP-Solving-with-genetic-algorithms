import itertools

# Example input (replace this with your actual city names and distances)
city_names = ["City1", "City2", "City3", "City4","City5","City6","City7","City8","City9"]
# Specific distances between cities
distances = {
    ("City1", "City2"): 10,
    ("City2", "City1"): 10,  # Ensure symmetry in distances
    ("City1", "City3"): 69,
    ("City3", "City1"): 69,  # Ensure symmetry in distances
    ("City1", "City4"): 5,
    ("City4", "City1"): 5,  # Ensure symmetry in distances
    ("City2", "City3"): 12,
    ("City3", "City2"): 12,  # Ensure symmetry in distances
    ("City2", "City4"): 18,
    ("City4", "City2"): 18,  # Ensure symmetry in distances
    ("City3", "City4"): 8,
    ("City4", "City3"): 8,   # Ensure symmetry in distances
    ("City1", "City5"): 25,
    ("City5", "City1"): 25,  # Ensure symmetry in distances
    ("City2", "City5"): 30,
    ("City5", "City2"): 30,  # Ensure symmetry in distances
    ("City3", "City5"): 35,
    ("City5", "City3"): 35,  # Ensure symmetry in distances
    ("City4", "City5"): 40,
    ("City5", "City4"): 40,  # Ensure symmetry in distances
    ("City1", "City6"): 28,
    ("City6", "City1"): 28,  # Ensure symmetry in distances
    ("City2", "City6"): 32,
    ("City6", "City2"): 32,  # Ensure symmetry in distances
    ("City3", "City6"): 76,
    ("City6", "City3"): 76,  # Ensure symmetry in distances
    ("City4", "City6"): 42,
    ("City6", "City4"): 42,  # Ensure symmetry in distances
    ("City5", "City6"): 45,
    ("City6", "City5"): 45,  # Ensure symmetry in distances
    ("City1", "City7"): 30,
    ("City7", "City1"): 30,  # Ensure symmetry in distances
    ("City2", "City7"): 35,
    ("City7", "City2"): 35,  # Ensure symmetry in distances
    ("City3", "City7"): 40,
    ("City7", "City3"): 40,  # Ensure symmetry in distances
    ("City4", "City7"): 45,
    ("City7", "City4"): 45,  # Ensure symmetry in distances
    ("City5", "City7"): 50,
    ("City7", "City5"): 50,  # Ensure symmetry in distances
    ("City6", "City7"): 55,
    ("City7", "City6"): 55,  # Ensure symmetry in distances
    ("City1", "City8"): 33,
    ("City8", "City1"): 33,  # Ensure symmetry in distances
    ("City2", "City8"): 78,
    ("City8", "City2"): 78,  # Ensure symmetry in distances
    ("City3", "City8"): 42,
    ("City8", "City3"): 42,  # Ensure symmetry in distances
    ("City4", "City8"): 47,
    ("City8", "City4"): 47,  # Ensure symmetry in distances
    ("City5", "City8"): 21,
    ("City8", "City5"): 21,  # Ensure symmetry in distances
    ("City6", "City8"): 57,
    ("City8", "City6"): 57,  # Ensure symmetry in distances
    ("City7", "City8"): 108,
    ("City8", "City7"): 108,  # Ensure symmetry in distances
    ("City1", "City9"): 35,
    ("City9", "City1"): 35,  # Ensure symmetry in distances
    ("City2", "City9"): 40,
    ("City9", "City2"): 40,  # Ensure symmetry in distances
    ("City3", "City9"): 99,
    ("City9", "City3"): 99,  # Ensure symmetry in distances
    ("City4", "City9"): 50,
    ("City9", "City4"): 50,  # Ensure symmetry in distances
    ("City5", "City9"): 555,
    ("City9", "City5"): 555,  # Ensure symmetry in distances
    ("City6", "City9"): 60,
    ("City9", "City6"): 60,  # Ensure symmetry in distances
    ("City7", "City9"): 60,
    ("City9", "City7"): 60,  # Ensure symmetry in distances
    ("City8", "City9"): 70,
    ("City9", "City8"): 70,  # Ensure symmetry in distances
}

def calculate_route_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances.get((route[i], route[i+1]), 0)
    return total_distance

all_possible_routes = []
# Generate all permutations of city orders
all_orders = itertools.permutations(city_names)

# Iterate through all permutations to calculate distances
for order in all_orders:
    total_distance = calculate_route_distance(order, distances)
    all_possible_routes.append((order, total_distance))

# Sort routes based on distance (best to worst)
sorted_routes = sorted(all_possible_routes, key=lambda x: x[1])

print("True optimal solution:")
print(sorted_routes[0])
# for route in sorted_routes:
#     print("Route:", route[0], "| Distance:", route[1])
