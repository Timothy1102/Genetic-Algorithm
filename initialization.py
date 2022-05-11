from input_constants import *
import random
from targets import Target
from sensors import Sensor


# note: the initialize functions may result in duplicated targets and sensors in the list at the current version

def init_targets():
    """initialize the targets points randomly."""
    targets_list = []
    for x in range(TARGETS_NUM): 
        target = Target(random.randint(0, DOMAIN_X), random.randint(0, DOMAIN_Y))
        targets_list.append(target)
    print("initialized targets, done! \n")
    return targets_list


def init_sensors_potential_positions():
    """initialize the potential positions to place sensors, randomly."""
    sensors_list = []
    for x in range(POTENTIAL_POSITONS):
        sensor = Sensor(random.randint(0, DOMAIN_X), random.randint(0, DOMAIN_Y))
        sensors_list.append(sensor)
    print("initialized sensors, done! \n")
    print("CALCULATING BEST SOLUTION... \n")
    return sensors_list



def print_targets(targets_list):
    for x in range(len(targets_list)):
        print("{x}: {target}".format(x=x+1, target=targets_list[x]))
    print("\n")

def print_sensors_potential_positions(sensors_list):
    for x in range(len(sensors_list)):
        print("{x}: {sensor}".format(x=x+1, sensor=sensors_list[x]))
    print("\n")



targets_list = init_targets()
sensors_list = init_sensors_potential_positions()

# print out the information
print("TARGETS LIST: ")
print_targets(targets_list)

print("SENSORS LIST: ")
print_sensors_potential_positions(sensors_list)