import sys
from transitions import Machine, State
from enum import Enum


class Model(object):

    class States(Enum):
        STATE_A = "stateA"
        STATE_B = "stateB"
        STATE_C = "stateC"

    def __init__(self):

        # Create a list of states
        states = [
            State(name=self.States.STATE_A,
                  on_enter=["on_enter_stateA"],
                  on_exit=["on_exit_stateA"]),
            State(name=self.States.STATE_B,
                  on_enter=["on_enter_stateB"],
                  on_exit=["on_exit_stateB"]),
            State(name=self.States.STATE_C,
                  on_enter=["on_enter_stateC"],
                  on_exit=["on_exit_stateC"]),
        ]

        # Create transitions
        transitions = [
            {
                "trigger": "fromAtoB",
                "source": self.States.STATE_A,
                "dest": self.States.STATE_B,
                "prepare": None,
                "before": None,
                "after": None,
                "conditions": None
            },
            {
                "trigger": "fromAtoC",
                "source": self.States.STATE_A,
                "dest": self.States.STATE_C,
                "prepare": None,
                "before": None,
                "after": None,
                "conditions": None
            },
            {
                "trigger": "fromBtoA",
                "source": self.States.STATE_B,
                "dest": self.States.STATE_A,
                "prepare": "prepare_fromBtoA",
                "before": "before_fromBtoA",
                "after": "after_fromBtoA",
                "conditions": "conditions_fromBtoA"
            },
            {
                "trigger": "toA",
                "source": "*",
                "dest": self.States.STATE_A,
                "prepare": None,
                "before": None,
                "after": None,
                "conditions": None
            },
        ]

        # Initialize the state machine
        self._machine = Machine(model=self,
                                states=states,
                                initial=self.States.STATE_A,
                                transitions=transitions)
        self._conditions = True

    def on_enter_stateA(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def on_exit_stateA(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def on_enter_stateB(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def on_exit_stateB(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def on_enter_stateC(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def on_exit_stateC(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def prepare_fromBtoA(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def before_fromBtoA(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def after_fromBtoA(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))

    def conditions_fromBtoA(self):
        print("do \"{}\" on \"{}\"".format(sys._getframe().f_code.co_name, self.state))
        self._conditions = not self._conditions
        print(" - conditions:\"{}\"".format(self._conditions))
        return self._conditions


if __name__ == "__main__":

    model = Model()
    print("state:[{}]".format(model.state))
    print("--- fromAtoB ---")
    model.fromAtoB()
    print("state:[{}]".format(model.state))
    print("--- fromBtoA ---")
    model.fromBtoA()
    print("state:[{}]".format(model.state))
    print("--- toA ---")
    model.toA()
    print("state:[{}]".format(model.state))
    print("--- fromAtoC ---")
    model.fromAtoC()
    print("state:[{}]".format(model.state))
    print("--- toA ---")
    model.toA()
    print("state:[{}]".format(model.state))
    print("--- fromAtoB ---")
    model.fromAtoB()
    print("state:[{}]".format(model.state))
    print("--- fromBtoA ---")
    model.fromBtoA()
    print("state:[{}]".format(model.state))
    print("--- toA ---")
    model.toA()
    print("state:[{}]".format(model.state))
