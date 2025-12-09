import re

def split_before_uppercases(formula):
    return re.findall(r'[A-Z][a-z]\d', formula)

def split_at_digit(element_string):
    match = re.match(r"([A-Za-z]+)(\d*)", element_string)
    if match:
        name = match.group(1)
        number_str = match.group(2)
        count = int(number_str) if number_str else 1
        return name, count
    return element_string, 1

def count_atoms_in_molecule(molecular_formula):
    atom_counts = {}
    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        atom_counts[atom_name] = atom_counts.get(atom_name, 0) + atom_count
    return atom_counts

def parse_chemical_reaction(reaction_equation):
    reaction_equation = reaction_equation.replace(" ", "")
    reactors, products = reaction_equation.split("->")
    return reactors.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
