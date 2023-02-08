from Stacks import Stacks
from Stack import Stack
from i import i
import os
import time
clear = lambda:os.system('cls')


def create_all_stacks(num_stacks, crate_letters_all):
    my_stacks = Stacks()
    for i in range(num_stacks):
        stack_num  = i+1
        crate_letters = crate_letters_all[i]
        stack_to_add = Stack(name=stack_num)
        stack_to_add.set_up_crates(crate_letters)
        my_stacks.add_stack(stack_to_add)
    return my_stacks


def get_instructions(i, stacks):
    instructions_split = i.split('\n')
    progress=0
    for instruction in instructions_split:
        ins_split_split = instruction.split(' ')

        num_crates_move = int(ins_split_split[1])
        from_stack = int(ins_split_split[3])
        to_stack = int(ins_split_split[-1])

        from_stack_crates = stacks.get_stack(from_stack).pop(num_pop=num_crates_move)
        for crate in from_stack_crates[::-1]:
            stacks.get_stack(to_stack).push(crate.get_value())
        print(f"Moved {[crate.get_value() for crate in from_stack_crates]} from {from_stack} to {to_stack}")
        progress+=1
        stacks.print_stacks()
        print(f"Progress {round(100*progress / len(instructions_split),2)}%")
        # time.sleep(0.01)
        # input('')
        clear()
        # print('\n\n')


    return stacks

crate_letters_all = ['RPCDBG','HVG','NSQDJPM','PSLGDCNM','JBNCPFLS','QBDZVGTS','BZMHFTQ','CMDBF','FCQG']
# crate_letters_all=['ZN','MCD','P']
num_stacks = len(crate_letters_all)
my_stacks = create_all_stacks(num_stacks, crate_letters_all)

print(f"START: \n")
my_stacks.print_stacks()
ss = get_instructions(
i=i, 
    stacks=my_stacks
)
ss.print_stacks()
