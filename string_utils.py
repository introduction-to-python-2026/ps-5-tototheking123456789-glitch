def split_before_each_uppercase(formula):
    if not formula:
        return []
    result = []
    start = 0
    for i in range(1, len(formula)):
        if formula[i].isupper():
            result.append(formula[start:i])
            start = i
    result.append(formula[start:])
    return result


def split_at_first_digit(fragment):
    i = 0
    while i < len(fragment) and not fragment[i].isdigit():
        i += 1
    if i == len(fragment):      
        return fragment, 1
    return fragment[:i], int(fragment[i:])


def count_atoms_in_molecule(formula):
    parts = split_before_each_uppercase(formula)
    counts = {}
    for part in parts:
        element, number = split_at_first_digit(part)
        counts[element] = counts.get(element, 0) + number
    return counts


def parse_chemical_reaction(reaction_equation):
    reaction_equation = reaction_equation.replace(" ", "")
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")


def count_atoms_in_reaction(molecules_list):
    return [count_atoms_in_molecule(molecule) for molecule in molecules_list]

