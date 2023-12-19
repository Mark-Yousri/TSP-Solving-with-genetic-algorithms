import matplotlib.pyplot as plt

def plot_fitness_and_population(fitness_values, generations):

    # Plotting fitness over generations
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(fitness_values)), fitness_values, label='Fitness')
    plt.title('Fitness over Generations')
    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.legend()
    plt.grid(True)
    plt.show()

