class Node:
    def __init__(self, data):
        self.children = []
        self.data = data # Node Data


def postorder(node):
    maximum = 0
    if len(node.children) > 0:
        child_size_total = 0
        child_total = 0
        for child in node.children:
            child_size, child_mean, child_max = postorder(child)
            child_size_total += child_size
            child_total += child_size * child_mean
            if child_max > maximum:
                maximum = child_max
        size = child_size_total + 1
        mean = (child_total + node.data) / (size)
        if mean > maximum:
            maximum = mean
    else:
        size = 1
        mean = node.data
        maximum = node.data
    return size, mean, maximum


z = int(input())
nodes = [Node(0)]
for y in range(z):
    line = input().strip()
    parent = int(line.split(" ")[0])
    value = int(line.split(" ")[1])
    new_node = Node(value)
    nodes.append(new_node)
    nodes[parent].children.append(new_node)
size, mean, maximum = postorder(nodes[0])
print(f'{maximum:.3f}')


