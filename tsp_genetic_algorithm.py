# Import necessary libraries
import random
from visualizations import plot_fitness_and_population

# Define TSP-related constants or configurations
# For example: number of cities, coordinates, distance matrix, etc.
class TSPConfig:
    def __init__(self, city_names, distances):
        self.city_names = city_names  # List of city names
        self.distances = distances  # Dictionary containing distances between cities

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


tsp_config = TSPConfig(city_names, distances)

class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = None

class Graph:
    def __init__(self, tsp_config):
        self.vertices = tsp_config.city_names
        self.adj_matrix = self._build_adjacency_matrix(tsp_config.distances)

    def _build_adjacency_matrix(self, distances):
        n = len(self.vertices)
        adj_matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                city_pair = (self.vertices[i], self.vertices[j])
                dist = distances.get(city_pair) or distances.get((city_pair[1], city_pair[0]))
                adj_matrix[i][j] = adj_matrix[j][i] = dist

        return adj_matrix

class GeneticAlgorithm:
    def __init__(self, tsp_config, population_size=100, crossover_rate=0.8, mutation_rate=0.2):
        self.tsp_config = tsp_config
        self.graph = Graph(tsp_config)
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.population = self._initialize_population()

    def _initialize_population(self):
        population = []
        for _ in range(self.population_size):
            chromosome = random.sample(self.graph.vertices, len(self.graph.vertices))
            individual = Individual(chromosome)
            population.append(individual)
        return population

    def evaluate_fitness(self, individual):
        total_distance = 0
        chromosome = individual.chromosome

        for i in range(len(chromosome) - 1):
            city1 = self.graph.vertices.index(chromosome[i])
            city2 = self.graph.vertices.index(chromosome[i + 1])
            total_distance += self.graph.adj_matrix[city1][city2]

        # Add distance from last city back to the starting city
        # city1 = self.graph.vertices.index(chromosome[-1])
        # city2 = self.graph.vertices.index(chromosome[0])
        # total_distance += self.graph.adj_matrix[city1][city2]
        individual.fitness = total_distance
        return total_distance

    def evaluate_population_fitness(self):
        for individual in self.population:
            self.evaluate_fitness(individual)

    def select_parents(self):
        return random.sample(self.population, 2)

    def crossover(self, parent1, parent2):
        # Implement ordered crossover
        offspring1, offspring2 = [], []
        size = len(parent1.chromosome)
        start, end = sorted(random.sample(range(size), 2))

        # Add genetic material from parents between start and end indices
        for i in range(start, end + 1):
            offspring1.append(parent1.chromosome[i])
            offspring2.append(parent2.chromosome[i])

        # Fill the rest of the offspring with the remaining genes from the other parent
        remaining1 = [gene for gene in parent2.chromosome if gene not in offspring1]
        remaining2 = [gene for gene in parent1.chromosome if gene not in offspring2]

        offspring1[end + 1:] = remaining1
        offspring2[end + 1:] = remaining2

        return Individual(offspring1), Individual(offspring2)

    def mutate(self, individual):
        # Implement swap mutation
        index1, index2 = random.sample(range(len(individual.chromosome)), 2)
        individual.chromosome[index1], individual.chromosome[index2] = (
            individual.chromosome[index2],
            individual.chromosome[index1],
        )

    def evolve(self):
        # Select parents, perform crossover, mutation, and replace population
        parents = self.select_parents()
        offspring1, offspring2 = self.crossover(parents[0], parents[1])

        if random.random() < self.mutation_rate:
            self.mutate(offspring1)
        if random.random() < self.mutation_rate:
            self.mutate(offspring2)

        offspring1_fitness = self.evaluate_fitness(offspring1)
        # print("offspring1 evaluation: "+ str(offspring1_fitness))
        offspring2_fitness = self.evaluate_fitness(offspring2)
        # print("offspring2 evaluation: "+ str(offspring2_fitness))

        worst_individuals = sorted(self.population, key=lambda x: x.fitness, reverse=True)[:2]
        # self.population.remove(worst_individuals[0])
        # self.population.remove(worst_individuals[1])
        # self.population.extend([offspring1, offspring2])

        # Replace worst individuals with offspring only if they are better
        if offspring1_fitness < worst_individuals[0].fitness:
            self.population.remove(worst_individuals[0])
            self.population.append(offspring1)

        if offspring2_fitness < worst_individuals[1].fitness: #population size did not matter
            self.population.remove(worst_individuals[1])
            self.population.append(offspring2)

    def run_genetic_algorithm(self, generations):
        fitness_values = []
        self.evaluate_population_fitness()
        for _ in range(generations):
        
            self.evolve()
             # Store the fitness of the best individual for this generation
            best_fitness = min(self.population, key=lambda x: x.fitness).fitness
            fitness_values.append(best_fitness)

        best_individual = min(self.population, key=lambda x: x.fitness)
        plot_fitness_and_population(fitness_values, generations)
        return best_individual.chromosome, best_individual.fitness
    
if __name__ == "__main__":
    # Code inside this block will execute when the script is run directly
    # Initialize TSPConfig, Graph, and GeneticAlgorithm instances
    tsp_config = TSPConfig(city_names, distances)
    genetic_algorithm = GeneticAlgorithm(tsp_config)

    # Run the genetic algorithm for a specific number of generations
    best_route, best_fitness = genetic_algorithm.run_genetic_algorithm(generations=1000)

    # Display or print the best route and its fitness
    print("Best Route:", best_route)
    print("Best Fitness:", best_fitness)