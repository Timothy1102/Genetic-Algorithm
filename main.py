import pygad
import numpy
from input_constants import *
from initialization import *
from targets import Target
from sensors import Sensor


targets_list = []
"""list of targets"""

sensors_list = []
"""list of sensors"""

w1 = 0.4
w2 = 0.35
w3 = 0.25

epochs = 40
"""number of epochs/generations"""

def on_start(ga_instance):
    global targets_list
    targets_list = init_targets()
    global sensors_list
    sensors_list = init_sensors_potential_positions()


def fitness_func(solution, solution_idx):
    # objective 1: minimize number of sensors
    positive_pos = 0
    for i in range(CHROMOSOME_LENGTH):
        if solution[i] == 1:
            positive_pos += 1
        objective1 = 1 - (positive_pos/POTENTIAL_POSITONS)

    # objective 2: K-coverage
    total_coverage = 0
    for i in range(TARGETS_NUM):
        k = 0
        for j in range(POTENTIAL_POSITONS):
            if solution[j] == 1:
                if sensors_list[j].sensing(targets_list[i]):
                    if k < K:
                        k += 1
        total_coverage = total_coverage + k
    objective2 = (total_coverage/(K*TARGETS_NUM))

    # object 3: M-connected
    total_connected = 0
    for i in range(POTENTIAL_POSITONS):
        if solution[i] == 1:
            m = 0
            for j in range(POTENTIAL_POSITONS):
                if solution[j] == 1 and i != j:
                    if sensors_list[i].communicating(sensors_list[j]):
                        if m < M:
                            m += 1
            total_connected = total_connected + m
    objective3 = (total_connected/(M*positive_pos))

    #  return the fitness value for a single solution
    return (w1*objective1 + w2*objective2 + w3*objective3)


# create an instance of the GA class in pygad package
# default parents selection: steady state selection
ga_instance = pygad.GA(num_generations=epochs,
                       num_parents_mating=2,
                       fitness_func=fitness_func,
                       sol_per_pop=30,
                       num_genes=CHROMOSOME_LENGTH,
                       gene_type=int,
                       init_range_low=0,
                       init_range_high=2,
                    #    parent_selection_type="rws",
                    #    crossover_probability=0.0001,
                    #    mutation_type="random",
                    #    random_mutation_min_val=0,
                    #    random_mutation_max_val=0,
                    #    mutation_probability=0.00003,
                       on_start=on_start,
                       save_best_solutions=True)


# ga_instance.initialize_population(low=0, high=2, allow_duplicate_genes=True, mutation_by_replacement=False, gene_type=int)
# print("population: \n {pop}".format(pop=ga_instance.population))

# run the pipeline 
ga_instance.run()

# print("population: \n {pop}".format(pop=ga_instance.population))
print("best solution fitness values over {epochs} generations: \n {best}".format(epochs=epochs, best=ga_instance.best_solutions_fitness))
print("\n")
print("the first best solution is in generation: {best}".format(best=ga_instance.best_solution_generation))
print("best solution in the last generation: \n {best}".format(best=ga_instance.best_solutions[epochs]))
print("\n")


def objective1_validation(solution):
    positive_pos = 0
    for i in range(CHROMOSOME_LENGTH):
        if solution[i] == 1:
            positive_pos += 1
        objective1 = 1 - (positive_pos/POTENTIAL_POSITONS)
    print("objective 1 fitness value (minimize sensors) for the best solution: {ob1}%".format(ob1=objective1*100))
    print("(positive positions = {ob})".format(ob=positive_pos))


def objective2_validation(solution):
    total_coverage = 0
    for i in range(TARGETS_NUM):
        k = 0
        for j in range(POTENTIAL_POSITONS):
            if solution[j] == 1:
                if sensors_list[j].sensing(targets_list[i]):
                    if k < K:
                        k += 1
        total_coverage = total_coverage + k
    objective2 = (total_coverage/(K*TARGETS_NUM))
    print("objective 2 fitness value (K-coverage) for the best solution = {ob2}%".format(ob2=objective2*100))


def objective3_validation(solution):
    total_connected = 0
    positive_pos = 0
    for i in range(CHROMOSOME_LENGTH):
        if solution[i] == 1:
            positive_pos += 1
    for i in range(POTENTIAL_POSITONS):
        if solution[i] == 1:
            m = 0
            for j in range(POTENTIAL_POSITONS):
                if solution[j] == 1 and i != j:
                    if sensors_list[i].communicating(sensors_list[j]):
                        if m < M:
                            m += 1
            total_connected = total_connected + m
    objective3 = (total_connected/(M*positive_pos))
    print("objective 3 fitness value (M-connected) for the best solution = {ob3}%".format(ob3=objective3*100))


best_solution = ga_instance.best_solutions[epochs]
objective1_validation(best_solution)
objective2_validation(best_solution)
objective3_validation(best_solution)

ga_instance.plot_fitness()


# parameters that affect the time to run: epochs, TARGETS_NUM, POTENTIAL_POSITIONS, sol_per_pop.