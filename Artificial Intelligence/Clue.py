from sympy import symbols
from sympy.logic.boolalg import And, Or, Not
from sympy.logic.inference import satisfiable
from termcolor import cprint  # For colored output

# Define logical symbols
mustard, plum, scarlet = symbols("ColMustard ProfPlum MsScarlet")
characters = [mustard, plum, scarlet]

ballroom, kitchen, library = symbols("ballroom kitchen library")
rooms = [ballroom, kitchen, library]

knife, revolver, wrench = symbols("knife revolver wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons  # Combine all symbols

# Define knowledge base (constraints)
knowledge = And(
    Or(mustard, plum, scarlet),  # One of these characters is guilty
    Or(ballroom, kitchen, library),  # Crime happened in one room
    Or(knife, revolver, wrench)  # The weapon used is one of these
)

# Function to check what is entailed
def check_knowledge(knowledge):
    for symbol in symbols:
        if satisfiable(And(knowledge, symbol)):  # Checking if symbol is true
            cprint(f"{symbol}: YES", "green")
        elif not satisfiable(And(knowledge, Not(symbol))):  # Can't prove either
            print(f"{symbol}: MAYBE")

# Display knowledge base
print(f"Knowledge Base: {knowledge}")

# Check knowledge
check_knowledge(knowledge)
