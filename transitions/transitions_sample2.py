from transitions.extensions import HierarchicalGraphMachine
from transitions.extensions import HierarchicalMachine
from transitions.extensions.nesting import NestedState
from PIL import Image
import os

# NestedState.separator = '/'

count_states = ['1', '2', '3', 'done']
count_trans = [
    ['increase', '1', '2'],
    ['increase', '2', '3'],
    ['decrease', '3', '2'],
    ['decrease', '2', '1'],
    ['done', '3', 'done'],
    ['reset', '*', '1']
]

counter = HierarchicalGraphMachine(
    states=count_states,
    transitions=count_trans,
    initial='1')

# states = ['waiting', 'collecting', {'name': 'counting', 'children': counter}]
# states = ['waiting', 'collecting', {'name': 'counting', 'children': counter, 'initial': False}]
states = ['waiting', 'collecting', {'name': 'counting', 'children': counter, 'remap': {'done': 'waiting'}}]

transitions = [
    ['collect', '*', 'collecting'],
    ['wait', '*', 'waiting'],
    ['count', 'collecting', 'counting']
]

collector = HierarchicalGraphMachine(
    states=states,
    transitions=transitions,
    initial='waiting')


def show():
    """
    image_name = "my_state_diagram.png"
    collector.get_graph().draw(image_name, prog='dot')
    path = os.getcwd()
    img = Image.open(path + "/" + image_name)
    """
    collector.get_graph().view()
    input("Please Enter: ")


print("--- initial ---")
print(" state:[{}]".format(collector.state))
show()

print("--- trans:collect ---")
collector.collect()  # collecting
print(" state:[{}]".format(collector.state))
show()

print("--- trans:count ---")
collector.count()  # let's see what we got; counting_1
print(" state:[{}]".format(collector.state))
show()

print("--- trans:increase ---")
collector.increase()  # counting_2
print(" state:[{}]".format(collector.state))
show()

print("--- trans:increase ---")
collector.increase()  # counting_3
print(" state:[{}]".format(collector.state))
show()

print("--- trans:done ---")
collector.done()  # collector.state == counting_done
print(" state:[{}]".format(collector.state))
show()

print("--- trans:wait ---")
collector.wait()  # collector.state == waiting
print(" state:[{}]".format(collector.state))
show()
