class Stacks:
    def __init__(self):
        self.all_stacks = []
    def add_stack(self, stack):
        self.all_stacks.append(stack)
    def get_stack(self, num):
        return self.all_stacks[num-1]
    def print_stacks(self):
        for s in self.all_stacks:
            print(f"{s.get_name()}: {s.print_stack()}")

