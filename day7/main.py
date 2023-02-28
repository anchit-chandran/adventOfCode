import re
import os

os.chdir('/day7')


class TreeNode:
    def __init__(self, value, size=None):
        self.value = value
        self.children = []
        self.size = size
        self.parent = None

    def add_children(self, child):
        child[0].parent = self
        self.children += child

    def __str__(self):
        return f"{self.value} (size={self.size})"

    def pprint(self, level=0):

        pprint_string = '\t'*level + self.value + f"({self.size})" + '\n'
        for child in self.children:
            pprint_string += child.pprint(level+1)
        return pprint_string

    def traverse(self):

        nodes_to_visit = [self]
        total = 0
        counter = 2

        while nodes_to_visit:

            # get the current node
            current_node = nodes_to_visit.pop()

            # if counter > 0:
            print(f"Current node: {current_node} Nodes to visit: {[node.value for node in nodes_to_visit]}")
                # counter-=1

            # get the nodes children, filter for directories that are empty, add to nodes to visit
            children = [child for child in current_node.children if child.size == None]
            nodes_to_visit += children

            # chceck current directory has no directories with unknown sizes. set size as sum if so
            if not children:
                # print('no empty directories. summing')
                total_size =  sum([child.size for child in current_node.children])
                if total_size < 100000:
                    print(f"Adding {current_node.value}'s size of {total_size}")
                    current_node.size = total_size
                    total += total_size
                else:
                    current_node.size = 0
            
            # current directory HAS unknown directories to visit so needed to come back
            # else:
                print('NEED TO COME BACK TO DIRECTORY')
                nodes_to_visit.insert(0,current_node)

            # print()
        return total

            





with open('i.txt', 'r') as f:
    i = [line.strip() for line in f.readlines()]

root = TreeNode('/')


def construct_tree(commands_list, root_node):

    current_dir = root_node

    for command in commands_list[1:]:
        # print(f"In current dir: {current_dir} with children {current_dir.children}")

        # command
        if command[0] == '$':

            # go back directory
            if command == '$ cd ..':
                # print(f"Go back directory to {current_dir.parent}")
                current_dir = current_dir.parent
            # enter directory
            elif command.startswith('$ cd '):
                prev_dir = current_dir
                for child in prev_dir.children:
                    if child.value == command[5:]:
                        current_dir = child
                # print(f'Changing directory: {current_dir.value}')
                # print(f"PREV DIRECTORY: {current_dir.parent}")
            # ls files
            else:
                # print(f'List all files')
                pass

        # just ls all files
        else:
            #  check if current item is a folder
            if command[0:3] == 'dir':
                folder_to_add = TreeNode(value=command[4:])
                # print(f"Appending folder {folder_to_add.value} to {current_dir.value}")
                current_dir.add_children([folder_to_add])

            # current item is a file
            else:
                patt = f"(\d+)\s(.+)"
                matches = re.search(patt, command)
                size = int(matches.group(1))
                name = matches.group(2)
                file_to_add = TreeNode(value=name, size=size)
                # print(f"Appending file {file_to_add.value}")
                current_dir.add_children([file_to_add])


construct_tree(i, root)
r = root.traverse() - 94853
print(root.pprint())
print(r)
