from copy import deepcopy
from Network.event import Event


class Table:

    def __init__(self, variables):
        self.__variables = variables
        self.__events = []

    def add_event(self, event):
        # Add an event to the table.
        self.__events.append(event)

    def update_event(self, old_event, prob):
        # This method will look into the current table and check if
        # it already has an entry for that event, and if it's true
        # will update its probability, otherwise will add a new
        # event to the table.
        for new_event in self.__events:
            if old_event.is_same_event(new_event):
                new_event.set_probability(new_event.probability()+old_event.probability())
            else:
                self.add_event(old_event)

    def sum_on_var(self, variable):
        # This method returns the sum of the probabilities entries with 'variable'.
        new_vars = deepcopy(self.__variables)
        # Remove variable from variables of the table
        new_vars.remove(variable)
        # Instantiate a new Table object
        new_table = Table(new_vars)
        # Updates the table with every event in the older table.
        for event in self.__events:
            # For each event in the old table make a copy of it without
            # the unwanted variable.
            aux_event = Event.deepcopy(event)
            aux_event.remove(variable)
            # Updates the table with the information for the old event
            # and the current information of the table.
            new_table.update_event(aux_event, aux_event.probability())
        return new_table

    def variables_in_common(self, other):
        # This method returns the variables in common between two table objects.
        return list(set(self.__variables).intersection(set(other.__variables)))

    def union_of_variables(self, other):
        # This method returns the union of variables in the two table objects.
        return list(set(self.__variables).union(set(other.__variables)))

    def multiply_tables(self, other):
        # This method returns a new table with the result of the multiplication of
        # the two entered tables.
        new_vars = self.union_of_variables(other)
        # Instantiate a new Table object
        new_table = Table(new_vars)

        for
        return 0

