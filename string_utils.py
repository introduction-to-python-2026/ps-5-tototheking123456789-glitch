import re

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
    m = re.match(r'^([A-Za-z]+)(\d*)$', fragment)
    if not m:
        if fragment.isdigit():
            return '', int(fragment)
        return '', 1
    element = m.group(1)
    number = int(m.group(2)) if m.group(2) else 1
    return element, number

def count_atoms_in_molecule(molecular_formula):
    if not molecular_formula:
        return {}
    m = re.match(r'^(\d+)(.*)$', molecular_formula)
    coeff = 1
    formula = molecular_formula
    if m:
        coeff = int(m.group(1))
        formula = m.group(2) or ''

    fragments = split_before_uppercases(formula)
    counts = {}
    for f in fragments:
        if not f:
            continue
        element, number = split_element_number(f)
        if element == '':
            continue
        counts[element] = counts.get(element, 0) + number
    if coeff != 1:
        for k in list(counts.keys()):
            counts[k] = counts[k] * coeff

    return counts

def parse_chemical_reaction(reaction_equation):
    if '->' in reaction_equation:
        lhs, rhs = reaction_equation.split('->', 1)
    elif '=>' in reaction_equation:
        lhs, rhs = reaction_equation.split('=>', 1)
    elif '=' in reaction_equation:
        lhs, rhs = reaction_equation.split('=', 1)
    else:
        raise ValueError("Reaction must contain an arrow like '->', '=>', or '='")
    reactants = lhs.split('+') if lhs else []
    products = rhs.split('+') if rhs else []
    return reactants, products

def count_atoms_in_reaction(molecules_list):
    total_counts = {}
    for molecule in molecules_list:
        atom_counts = count_atoms_in_molecule(molecule)
        for atom, count in atom_counts.items():
            total_counts[atom] = total_counts.get(atom, 0) + count
    return total_counts
