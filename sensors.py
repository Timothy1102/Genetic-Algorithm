from targets import Target
from scipy.spatial import distance
from input_constants import *

class Sensor:
    """
    represents a sensor node
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({x}, {y})".format(x=self.x, y=self.y)


    def sensing(self, target):
        dist = distance.euclidean([self.x, self.y], [target.x, target.y])
        if dist <= SENSING_RANGE :
            # print("sensable this target")
            return True
        else:
            return False

    def communicating(self, sensor):
        dist = distance.euclidean([self.x, self.y], [sensor.x, sensor.y])
        if dist <= COMMUNICATION_RANGE :
            # print("communicating with this sensor")
            return True
        else:
            return False

