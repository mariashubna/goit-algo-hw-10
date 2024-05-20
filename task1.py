import pulp

model = pulp.LpProblem("Maximize Products", pulp.LpMaximize)

Lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  
Juice = pulp.LpVariable('Juice', lowBound=0, cat='Integer')  

model += Lemonade + Juice, "Total Products"

model += 2 * Lemonade + 1 * Juice <= 100, "Water Constraint"  
model += 1 * Lemonade <= 50, "Sugar Constraint"  
model += 1 * Lemonade <= 30, "Lemon Juice Constraint"  
model += 2 * Juice <= 40, "Fruit Puree Constraint"  

model.solve()

# pulp.LpStatus[model.status]

print("Виробляти лимонад:", Lemonade.varValue)
print("Виробляти фруктовий сік:", Juice.varValue)
