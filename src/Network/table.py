from copy import deepcopy
from Network.event import Event


class Table:

    def __init__(self, variables):
        self.__variables = variables
        self.__events = []

    def add_event(self, event):
        self.__events.append(event)

    def sum_on_var(self, variable):
        #
        return Table.table_without_var(self, variable)

    def multiply_tables(self, other):
        return 0

    def update_event(self, old_event, prob):
        for new_event in self.__events:
            if old_event.is_same_event(new_event):
                new_event.set_probability(new_event.probability()+old_event.probability())
            else:
                self.add_event(old_event)

    @staticmethod
    def table_without_var(self, table, variable):
        # This method copies 'table' and returns a new table without 'variable'.
        new_vars = deepcopy(table.__variables)
        # Remove variable from variables of the table
        new_vars.remove(variable)
        # Instantiate a new Table object
        new_table = Table(new_vars)
        # Update thje
        for event in table.__events:
            aux_event = Event.deepcopy(event)
            aux_event.remove(variable)
            new_table.update_event(aux_event, aux_event.probability())

