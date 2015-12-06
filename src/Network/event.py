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

    def variables(self):
        return list(self.__event.keys())

    def set_probability(self, probability):
        self.__probability = probability

    def probability(self):
        return self.__probability

    def get_value(self, var):
        return self.__event[var]

    def get_values_from_variables(self, variables):
        res = []
        for var in variables:
            res.append(self.__event[var])
        return res

    def remove_var(self, var):
        del self.__event[var]

    def is_same_event(self, other):
        for variable in self.__event.keys():
            if self.__event[variable] != other.__event[variable]:
                return False
        return True

    def combine_events(self, other):
        # This method receives two events and returns a dictionary with the full event.
        res = {}
        for x1 in self.variables():
            res[x1] = self.__event.get(x1)
        for x2 in other.variables():
            res[x2] = self.__event.get(x2)
        return res

    @staticmethod
    def deepcopy(other):
        new_event = deepcopy(other.__event)
        return Event(new_event, other.__probability)

    def __repr__(self):
        return 'Event: ' + str(self.__event) + '; Prob: ' + str(self.__probability)