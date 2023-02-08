class Crate:
    def __init__(self, value, next_crate = None):
        self.value = value
        self.next_crate = None
    # see crate letter
    def get_value(self):
        return self.value
    
    # set next crate
    def set_next_crate(self, next_crate):
        self.next_crate = next_crate
    
    # get next create
    def get_next_crate(self):
        return self.next_crate