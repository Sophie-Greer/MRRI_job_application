from statemachine import StateMachine, State

class VariableX(StateMachine):
    noNumber = State(initial = True)
    numberX = float(input("Provide a decimal between 1 and 20 (inclusive): "))

    if numberX % 2.0 != 0.0:
        numberX = numberX + 1.0

        if numberX > 10.0:
            print("TOO BIG!")
            noNumber = State()

    else:
        numberX = (numberX + 10.0) / 2.0

        if numberX < 10.0:
            print("too small")
            State = noNumber

        else:
          finalState = State()

    if numberX > 10.0 and numberX % 2.0 == 0.0:
        finalState = State()
        print("Great choice!")

VariableX()
