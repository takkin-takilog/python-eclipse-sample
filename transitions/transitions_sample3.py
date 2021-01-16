from PIL import Image
import os
import sys
from enum import Enum, auto
from transitions.extensions.nesting import NestedState
from transitions.extensions.states import Timeout, Tags, add_state_features
from transitions.extensions.factory import HierarchicalGraphMachine
from transitions import Machine, State


class Model(object):

    class ChildStates(Enum):
        waiting = auto()
        trading = auto()
        updating = auto()

    class ParentStates(Enum):
        normal = auto()
        abnormal = auto()

    def __init__(self):

        NAME = "name"
        CHILDREN = "children"
        ON_ENTER = "on_enter"
        ON_EXIT = "on_exit"
        TRIGGER = "trigger"
        SOURCE = "source"
        DEST = "dest"
        PREPARE = "prepare"
        BEFORE = "before"
        AFTER = "after"
        CONDITIONS = "conditions"

        c_states = [
            {
                NAME: self.ChildStates.waiting,
                ON_ENTER: "on_enter_waiting",
                ON_EXIT: "on_exit_waiting"
            },
            {
                NAME: self.ChildStates.trading,
                ON_ENTER: "on_enter_trading",
                ON_EXIT: "on_exit_trading"
            },
            {
                NAME: self.ChildStates.updating,
                ON_ENTER: "on_enter_updating",
                ON_EXIT: "on_exit_updating"
            }
        ]

        c_transitions = [
            {
                TRIGGER: "trans_from_waiting_to_trading",
                SOURCE: self.ChildStates.waiting,
                DEST: self.ChildStates.trading,
                PREPARE: "prepare_from_waiting_to_trading",
                BEFORE: "before_from_waiting_to_trading",
                AFTER: "after_from_waiting_to_trading",
                CONDITIONS: None
            },
            {
                TRIGGER: "trans_from_trading_to_waiting",
                SOURCE: self.ChildStates.trading,
                DEST: self.ChildStates.waiting,
                PREPARE: "prepare_from_trading_to_waiting",
                BEFORE: "before_from_trading_to_waiting",
                AFTER: "after_from_trading_to_waiting",
                CONDITIONS: None
            },
            {
                TRIGGER: "trans_from_waiting_to_updating",
                SOURCE: self.ChildStates.waiting,
                DEST: self.ChildStates.updating,
                PREPARE: "prepare_from_waiting_to_updating",
                BEFORE: "before_from_waiting_to_updating",
                AFTER: "after_from_waiting_to_updating",
                CONDITIONS: None
            },
            {
                TRIGGER: "trans_from_updating_to_waiting",
                SOURCE: self.ChildStates.updating,
                DEST: self.ChildStates.waiting,
                PREPARE: "prepare_from_updating_to_waiting",
                BEFORE: "before_from_updating_to_waiting",
                AFTER: "after_from_updating_to_waiting",
                CONDITIONS: None
            },
        ]

        c_machine = HierarchicalGraphMachine(
            states=c_states,
            initial=self.ChildStates.waiting,
            transitions=c_transitions)

        p_states = [
            {
                NAME: self.ParentStates.normal,
                CHILDREN: c_machine,
                ON_ENTER: "on_enter_normal",
                ON_EXIT: "on_exit_normal"
            },
            {
                NAME: self.ParentStates.abnormal,
                ON_ENTER: "on_enter_abnormal",
                ON_EXIT: "on_exit_abnormal"
            }
        ]

        p_transitions = [
            {
                TRIGGER: "trans_from_normal_to_abnormal",
                SOURCE: self.ParentStates.normal,
                DEST: self.ParentStates.abnormal,
                PREPARE: "prepare_from_normal_to_abnormal",
                BEFORE: "before_from_normal_to_abnormal",
                AFTER: "after_from_normal_to_abnormal",
                CONDITIONS: None
            },
            {
                TRIGGER: "trans_from_abnormal_to_normal",
                SOURCE: self.ParentStates.abnormal,
                DEST: self.ParentStates.normal,
                PREPARE: "prepare_from_abnormal_to_normal",
                BEFORE: "before_from_abnormal_to_normal",
                AFTER: "after_from_abnormal_to_normal",
                CONDITIONS: None
            },
        ]

        self._p_machine = HierarchicalGraphMachine(
            model=self,
            states=p_states,
            initial=self.ParentStates.normal,
            transitions=p_transitions)

    def on_enter_waiting(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def on_exit_waiting(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def on_enter_trading(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def on_exit_trading(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def on_enter_updating(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def on_exit_updating(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def on_enter_normal(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def on_exit_normal(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def on_enter_abnormal(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def on_exit_abnormal(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def prepare_from_waiting_to_trading(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def before_from_waiting_to_trading(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def after_from_waiting_to_trading(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def prepare_from_trading_to_waiting(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def before_from_trading_to_waiting(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def after_from_trading_to_waiting(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def prepare_from_waiting_to_updating(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def before_from_waiting_to_updating(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def after_from_waiting_to_updating(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def prepare_from_updating_to_waiting(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def before_from_updating_to_waiting(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def after_from_updating_to_waiting(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def prepare_from_normal_to_abnormal(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def before_from_normal_to_abnormal(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def after_from_normal_to_abnormal(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def prepare_from_abnormal_to_normal(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def before_from_abnormal_to_normal(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def after_from_abnormal_to_normal(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

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
    print(" is_normal:[{}]".format(m.is_normal(allow_substates=True)))
    m.show()

    print("--- trans_from_normal_to_abnormal ---")
    m.trans_from_normal_to_abnormal()
    print(" state:[{}]".format(m.state))
    print(" is_normal:[{}]".format(m.is_normal(allow_substates=True)))
    m.show()

    print("--- trans_from_abnormal_to_normal ---")
    m.trans_from_abnormal_to_normal()
    print(" state:[{}]".format(m.state))
    print(" is_normal:[{}]".format(m.is_normal(allow_substates=True)))
    m.show()

    print("--- trans_from_waiting_to_trading ---")
    m.trans_from_waiting_to_trading()
    print(" state:[{}]".format(m.state))
    print(" is_normal:[{}]".format(m.is_normal(allow_substates=True)))
    m.show()

    print("--- trans_from_trading_to_waiting ---")
    m.trans_from_trading_to_waiting()
    print(" state:[{}]".format(m.state))
    print(" is_normal:[{}]".format(m.is_normal(allow_substates=True)))
    m.show()

    print("--- trans_from_waiting_to_updating ---")
    m.trans_from_waiting_to_updating()
    print(" state:[{}]".format(m.state))
    print(" is_normal:[{}]".format(m.is_normal(allow_substates=True)))
    m.show()

    print("--- trans_from_updating_to_waiting ---")
    m.trans_from_updating_to_waiting()
    print(" state:[{}]".format(m.state))
    print(" is_normal:[{}]".format(m.is_normal(allow_substates=True)))
    m.show()

    print("--- trans_from_waiting_to_trading ---")
    m.trans_from_waiting_to_trading()
    print(" state:[{}]".format(m.state))
    print(" is_normal:[{}]".format(m.is_normal(allow_substates=True)))
    m.show()

    print("--- trans_from_normal_to_abnormal ---")
    m.trans_from_normal_to_abnormal()
    print(" state:[{}]".format(m.state))
    print(" is_normal:[{}]".format(m.is_normal(allow_substates=True)))
    m.show()

    print("--- trans_from_abnormal_to_normal ---")
    m.trans_from_abnormal_to_normal()
    print(" state:[{}]".format(m.state))
    print(" is_normal:[{}]".format(m.is_normal(allow_substates=True)))
    m.show()
