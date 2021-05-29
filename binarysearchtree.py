# Binary search algorithm/tree

# When the user inputs a random number, the program will check if that number is included in the list. 
# It will do so by creating two halves of the list. If the program finds the number in the first half of the list, 
# it will eliminate the other half and vice versa. 
# The search will continue until the program finds the number input of the user or 
# until the subarray size becomes 0 (this means that the number is not in the list). 
# This python project idea will help you create an implement an algorithm that searches for an element in a list. 



import argparse
import random


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, list_of_values):
        self.root = Node(list_of_values.pop())

        for new_value in list_of_values:
            self._insert_node(self.root, new_value)

    def _insert_node(self, current_node, new_value):

        if new_value <= current_node.value:
            if current_node.left == None:
                current_node.left = Node(new_value)
            else:
                self._insert_node(current_node.left, new_value)
        else:
            if current_node.right == None:
                current_node.right = Node(new_value)
            else:
                self._insert_node(current_node.right, new_value)

    def insert_node(self, value):
        self._insert_node(self.root, value)
    
    def _contains(self, current_node, value):

        if value < current_node.value:
            return self._contains(current_node.left, value)
        elif value > current_node.value:
            return self._contains(current_node.right, value)
        elif value == current_node:
            return True
        else:
            return False

    def contains(self, value):
        return self._contains(self.root, value)

def parse_args():
    parser = argparse.ArgumentParser()
    # remember to run 'python3 binarysearchtree.py -n number_of_elements'
    parser.add_argument('-n', dest='number_of_elements', type=int,
                        required=True, help='# of values in binary search tree')
    return parser.parse_args()


def main():
    args = parse_args()

    print(args.number_of_elements)

    number_list = []
    for i in range(0, args.number_of_elements):
        number_list.append(random.randint(0, 200))

    print(number_list)

    my_tree = BinarySearchTree(number_list)
    
    # change random.randint(0, 100) to an integer if searching for a specific integer
    # could change integer to be user input as well
    print(my_tree.contains(random.randint(0, 100)))


if __name__ == '__main__':
    main()