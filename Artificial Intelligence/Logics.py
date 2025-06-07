from sympy import symbols
from sympy.logic.boolalg import And, Or, Not, Implies
from sympy.logic.inference import satisfiable

# creating logical symbols
rain = symbols ("rain") # It is raining.
hagrid = symbols("hagrid") # Harry visited Hagrid.
dumbledore = symbols("dumbledore") # Harry visited Dumbledore.

sentence = And(rain, hagrid) # It is raining and Harry visited Hagrid.
print(sentence)  # Output: rain & hagrid

Knowledge = Implies(Not(rain), hagrid) # If it is not raining, then Harry visited Hagrid.
print(Knowledge)  # Output: ~rain -> hagrid

Knowledge = And(
    Implies(Not(rain), hagrid),    # If it is not raining, then Harry visited Hagrid.
    Or(hagrid, dumbledore),        # Harry visited either Hagrid or Dumbledore
    Not(And(hagrid, dumbledore)),  # Harry did not visit both Hagrid and Dumbledore.
    dumbledore                     # Harry visited Dumbledore.
)  
print(Knowledge)  # Output: dumbledore & (dumbledore | hagrid) & (Implies(~rain, hagrid)) & ~(dumbledore & hagrid)

# Premises: If it rains, then Harry visits Hagrid
premise = Implies(rain, hagrid)

# Conclusion: Harry visits Hagrid
conclusion = hagrid

# Check if premises entail the conclusion
entailment_check = satisfiable(And(premise, ~conclusion)) 
# This means that in every case where the premises are true, the conclusion must be true as well.
#  this means AND of Negation will be false

print(entailment_check) 

# If entailment_check is False, it means the premise entails the conclusion
if not entailment_check:
    print("Premises entail the conclusion (⊨).")
else:
    print("Premises do not entail the conclusion (⊭).")