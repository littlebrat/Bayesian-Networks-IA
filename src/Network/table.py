from copy import deepcopy
from Network.event import Event


class Table:

    def __init__(self, variables):
        self.__variables = variables
        self.__events = []

    def add_event(self, event):
        # Add an event to the table.
        self.__events.append(event)

    def remove_event(self, event):
        # Remove certain event from the table.
        self.__events.remove(event)

    def has_variable(self, variable):
        # Returns a boolean depending if it has the variable in the table.
        return variable in self.__variables

    def evidence_eliminate(self, evidences):
        # Eliminate events that have the same values for the
        # variables as the evidence.
        new_events = []
        for event in self.__events:
            is_good_event = True
            for evidence in evidences.keys():
                if self.has_variable(evidence) and event.get_value(evidence) != evidences[evidence]:
                    is_good_event = False
            if is_good_event:
                 new_events.append(event)
        self.__events = new_events

    def update_event(self, old_event):
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
            aux_event.remove_var(variable)
            # Updates the table with the information for the old event
            # and the current information of the table.
            new_table.update_event(aux_event)
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
        common_vars = self.variables_in_common(other)
        # Creates a new factor with information from the other two previous tables.
        new_table = Table(new_vars)
        for first_event in self.__events:
            for second_event in other.__events:
                if first_event.get_values_from_variables(common_vars) == second_event.get_values_from_variables(common_vars):
                    # Find the appropriate event for this combination of variables.
                    aux_dict = first_event.combine_events(second_event)
                    # Add the newly found event to the new factor table.
                    new_table.add_event(Event(aux_dict, first_event.probability() * second_event.probability()))
        return new_table

    @staticmethod
    def deepcopy(other):
        t = Table(deepcopy(other.__variables))
        for e in other.__events:
            t.add_event(Event.deepcopy(e))
        return t

    def __repr__(self):
        r = 'Vars: ' + str(self.__variables) + '\n'
        for x in self.__events:
            r += str(x) + '\n'
        return r[:-1]