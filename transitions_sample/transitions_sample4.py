from PIL import Image
import os
import sys
import logging
from enum import Enum, auto
from transitions.extensions.factory import HierarchicalGraphMachine
from transitions.extensions.nesting import HierarchicalMachine


class Model(object):

    class States(Enum):
        A = auto()
        B = auto()

    class Child1States(Enum):
        a = auto()
        b = auto()
        c = auto()

    class Child2States(Enum):
        x = auto()
        y = auto()
        z = auto()

    def __init__(self):

        NAME = "name"
        CHILDREN = "children"
        PARALLEL = "parallel"
        ON_ENTER = "on_enter"
        ON_EXIT = "on_exit"
        TRIGGER = "trigger"
        SOURCE = "source"
        DEST = "dest"
        PREPARE = "prepare"
        BEFORE = "before"
        AFTER = "after"
        CONDITIONS = "conditions"

        logging.basicConfig(level=logging.INFO)

        # -------------------- Child[1] State Machine --------------------
        c1_states = [
            {
                NAME: Model.Child1States.a,
                ON_ENTER: None,
                ON_EXIT: None
            },
            {
                NAME: Model.Child1States.b,
                ON_ENTER: None,
                ON_EXIT: None
            },
            {
                NAME: Model.Child1States.c,
                ON_ENTER: None,
                ON_EXIT: None
            }
        ]

        c1_transitions = [
            {
                TRIGGER: "trans_from_a_to_b",
                SOURCE: Model.Child1States.a,
                DEST: Model.Child1States.b,
                PREPARE: None,
                BEFORE: None,
                AFTER: None,
                CONDITIONS: None
            },
            {
                TRIGGER: "trans_from_b_to_c",
                SOURCE: Model.Child1States.b,
                DEST: Model.Child1States.c,
                PREPARE: None,
                BEFORE: None,
                AFTER: None,
                CONDITIONS: None
            },
            {
                TRIGGER: "trans_from_c_to_a",
                SOURCE: Model.Child1States.c,
                DEST: Model.Child1States.a,
                PREPARE: None,
                BEFORE: None,
                AFTER: None,
                CONDITIONS: None
            },
        ]

        c1_machine = HierarchicalGraphMachine(
            states=c1_states,
            initial=Model.Child1States.a,
            transitions=c1_transitions)

        # -------------------- Child[2] State Machine --------------------
        c2_states = [
            {
                NAME: Model.Child2States.x,
                ON_ENTER: None,
                ON_EXIT: None
            },
            {
                NAME: Model.Child2States.y,
                ON_ENTER: None,
                ON_EXIT: None
            },
            {
                NAME: Model.Child2States.z,
                ON_ENTER: None,
                ON_EXIT: None
            }
        ]

        c2_transitions = [
            {
                TRIGGER: "trans_from_x_to_y",
                SOURCE: Model.Child2States.x,
                DEST: Model.Child2States.y,
                PREPARE: None,
                BEFORE: None,
                AFTER: None,
                CONDITIONS: None
            },
            {
                TRIGGER: "trans_from_y_to_z",
                SOURCE: Model.Child2States.y,
                DEST: Model.Child2States.z,
                PREPARE: None,
                BEFORE: None,
                AFTER: None,
                CONDITIONS: None
            },
            {
                TRIGGER: "trans_from_z_to_x",
                SOURCE: Model.Child2States.z,
                DEST: Model.Child2States.x,
                PREPARE: None,
                BEFORE: None,
                AFTER: None,
                CONDITIONS: None
            },
        ]

        c2_machine = HierarchicalGraphMachine(
            states=c2_states,
            initial=Model.Child2States.x,
            transitions=c2_transitions)

        # -------------------- Parent State Machine --------------------
        p_states = [
            {
                NAME: Model.States.A,
                PARALLEL: [
                    {
                        NAME: "1",
                        CHILDREN: c1_machine
                    },
                    {
                        NAME: "2",
                        CHILDREN: c2_machine
                    }
                ],
                ON_ENTER: None,
                ON_EXIT: None
            },
            {
                NAME: Model.States.B,
                ON_ENTER: None,
                ON_EXIT: None
            }
        ]

        p_transitions = [
            {
                TRIGGER: "trans_from_A_to_B",
                SOURCE: Model.States.A,
                DEST: Model.States.B,
                PREPARE: None,
                BEFORE: None,
                AFTER: None,
                CONDITIONS: None
            },
            {
                TRIGGER: "trans_from_B_to_A",
                SOURCE: Model.States.B,
                DEST: Model.States.A,
                PREPARE: None,
                BEFORE: None,
                AFTER: None,
                CONDITIONS: None
            },
        ]

        self._p_machine = HierarchicalGraphMachine(
            model=self,
            states=p_states,
            initial=Model.States.A,
            transitions=p_transitions)

    def show(self):
        """
        image_name = "my_state_diagram.png"
        self._p_machine.get_graph().draw(image_name, prog='dot')
        path = os.getcwd()
        img = Image.open(path + "/" + image_name)
        """
        self._p_machine.get_graph().view()
        input("Please Enter: ")


if __name__ == "__main__":

    m = Model()

    print("--- initial ---")
    print(" state:[{}]".format(m.state))
    print(" is_A:[{}]".format(m.is_A(allow_substates=False)))
    print(" is_a:[{}]".format(m.is_A_1_a(allow_substates=False)))
    print(" is_x:[{}]".format(m.is_A_2_x(allow_substates=False)))
    m.show()

    print("--- trans_from_A_to_B ---")
    m.trans_from_A_to_B()
    print(" state:[{}]".format(m.state))
    print(" is_A:[{}]".format(m.is_A(allow_substates=False)))
    m.show()

    print("--- trans_from_B_to_A ---")
    m.trans_from_B_to_A()
    print(" state:[{}]".format(m.state))
    print(" is_A:[{}]".format(m.is_A(allow_substates=False)))
    m.show()

    print("--- trans_from_a_to_b ---")
    m.trans_from_a_to_b()
    print(" state:[{}]".format(m.state))
    # print(" is_normal:[{}]".format(m.is_A(allow_substates=True)))
    m.show()

    print("--- trans_from_x_to_y ---")
    m.trans_from_x_to_y()
    print(" state:[{}]".format(m.state))
    # print(" is_normal:[{}]".format(m.is_A(allow_substates=True)))
    m.show()

    print("--- trans_from_A_to_B ---")
    m.trans_from_A_to_B()
    print(" state:[{}]".format(m.state))
    # print(" is_normal:[{}]".format(m.is_A(allow_substates=True)))
    m.show()

    print("--- trans_from_B_to_A ---")
    m.trans_from_B_to_A()
    print(" state:[{}]".format(m.state))
    # print(" is_normal:[{}]".format(m.is_A(allow_substates=True)))
    m.show()
