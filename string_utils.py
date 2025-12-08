def split_before_uppercases(formula):
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

def split_element_number(fragment):
    i = 0
    while i < len(fragment) and not fragment[i].isdigit():
        i += 1
    element = fragment[:i]
    number = int(fragment[i:]) if i < len(fragment) else 1
    return element, number

def count_atoms_in_molecule(molecular_formula):
    fragments = split_before_uppercases(molecular_formula)
    d = {}
    for f in fragments:
        element, number = split_element_number(f)
        d[element] = number
    return d


def parse_chemical_reaction(reaction_equation):
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")


def count_atoms_in_reaction(molecules_list):
    total_counts = {}
    for molecule in molecules_list:
        atom_counts = count_atoms_in_molecule(molecule)
        for atom, count in atom_counts.items():
            if atom in total_counts:
                total_counts[atom] += count
            else:
                total_counts[atom] = count
    return total_counts
