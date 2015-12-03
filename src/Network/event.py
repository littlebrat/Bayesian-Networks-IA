from copy import deepcopy


class Event:
    """
        This class defines an event from a probability table.
        It stores the values from its variables in a dictionary and the probability of occurrence of this
        event is given by a float.
    """

    def __init__(self, event, probability):
        self.__probability = probability
        self.__event = event

    def set_probability(self, probability):
        self.__probability = probability

    def probability(self):
        return self.__probability

    def get_value(self, var):
        return self.__event[var]

    def remove_var(self, var):
        del self.__event[var]

    def is_same_event(self, other):
        for variable in self.__event.keys():
            if self.__event[variable] != other.__event[variable]:
                return False
        return True

    @staticmethod
    def deepcopy(other):
        new_event = deepcopy(other.__event)
        return Event(new_event, other.__probability)
