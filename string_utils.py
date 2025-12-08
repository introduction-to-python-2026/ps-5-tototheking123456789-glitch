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
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
