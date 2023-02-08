from Crate import Crate

class Stack:
    def __init__(self, name):
        self.head = None
        self.size = 0
        self.name = name
    
    def get_name(self):
        return self.name

    def is_empty(self):
        return self.size == 0

    def push(self, next_crate_val):
        if not self.is_empty():
            # print(f'Adding {next_crate_val}')
            self.size += 1

            current_top_crate = self.head
            self.head = Crate(value = next_crate_val)
            self.head.set_next_crate(current_top_crate)

            # print(f"{self.head.get_value()} -> {current_top_crate.get_value()}")

        else:
            # print(f'Empty stack! Adding new head {next_crate_val}')
            self.head = Crate(next_crate_val)
            self.size+=1
    
    def pop(self, num_pop):
        if not self.is_empty():
            self.crates_to_pop = []
            for _ in range(num_pop):
                crate_to_pop = self.head
                self.head = crate_to_pop.get_next_crate()
                self.crates_to_pop.append(crate_to_pop)
            return self.crates_to_pop
        else:
            print('No crates in stack!')

    def peek(self):
        return self.head.get_value()
    
    def set_up_crates(self,crate_letters):
        for l in [letter for letter in crate_letters]:
            # print(f'adding letter: {l}')
            self.push(l)
    
    def print_stack(self):
        if not self.is_empty():
            pointer_var = self.head
            self.stack_list = []
            while pointer_var != None:
                pointer_var_value = pointer_var.get_value()
                # print(f"Currently pointer on {pointer_var_value}. Appending...")
                self.stack_list.append(pointer_var_value)
                pointer_var = pointer_var.get_next_crate()
            return f"{self.stack_list[::-1]}<- HEAD"
        else:
            print('Empty stack!')
