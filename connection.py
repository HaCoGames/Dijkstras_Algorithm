import position

class Connection:
    def __init__(self, position1, position2, time):
        self.position1 = position1
        self.position2 = position2
        self.time = time
    
    def __str__(self):
        return str(self.position1) + " " + str(self.position2) + " " + str(self.time)
    
    def __repr__(self):
        return str(self.position1) + " " + str(self.position2) + " " + str(self.time)
    
    def get_position1(self):
        return self.position1
    
    def get_position2(self):
        return self.position2
    
    def get_time(self):
        return self.time
    
    def set_time(self, time):
        self.time = time

    def is_valid(self, position1, position2):
        if self.position1 == position1 and self.position2 == position2:
            return True
        elif self.position1 == position2 and self.position2 == position1:
            return True
        else:
            return False