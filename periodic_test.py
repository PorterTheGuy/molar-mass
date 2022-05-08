import periodictable

inputs = []
while True:
    inp = input("What would you like to add? ")
    if inp == "":
        break
    inputs.append(inp)

answers = []
for inp in inputs:
    masses = periodictable.elements.symbol(inp).mass
    answers.append(masses)

print("Your elements are " + str(sum(answers)) + " g/mol")