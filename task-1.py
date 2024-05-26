import pulp

model = pulp.LpProblem("Maximize_Output", pulp.LpMaximize)

# Goods
L = pulp.LpVariable('L', lowBound=0, cat='Integer') # Limonade
F = pulp.LpVariable('F', lowBound=0, cat='Integer') # Fruit Juice

model += L + F, "Output"

# Resourses
model += 2*L + F <= 100 # Water
model += L <= 50 # Sugar
model += L <= 30 # Limone's juice
model += 2*F <= 40 # Fruit's puree

model.solve()

# Result
print(f"Maximum Output is {L.varValue} Limonade and {F.varValue} Fruit Juice")