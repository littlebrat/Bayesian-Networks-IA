

class Logger:

    def __init__(self):
        self.my_log = '\n \n########## STEPS ########## \n \n'

    def log_it(self, other_data):
        self.my_log += other_data + '\n \n'

    def __repr__(self):
        return self.my_log