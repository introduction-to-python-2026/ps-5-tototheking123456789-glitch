

    return formula[:digit_location], int(formula[digit_location:])
def split_before_each_uppercases(formula):
  if not formula:
    return []
  result = []
  start = 0
  end = 1
  for char in formula[1:]:
    if char.isupper():
      result.append(formula[start:end])
      start = end
    end += 1
  result.append(formula[start:])
  return result


def split_at_first_digit(formula):
    digit_location = 1
    for char in formula[1:]:
      if char.isdigit():
        break 
      digit_location += 1
    if digit_location == len(formula):
      return formula, 1


def count_atoms_in_molecule(formula):
    counts = {}
    i = 0
    while i < len(formula):
        element = formula[i]
        i += 1
        if i < len(formula) and formula[i].islower():
            element += formula[i]
            i += 1
        num = ""
        while i < len(formula) and formula[i].isdigit():
            num += formula[i]
            i += 1
        num = int(num) if num else 1  # default amount is 1
        counts[element] = counts.get(element, 0) + num
    return counts


    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)
        
        # Step 2: Update the dictionary with the atom name and count

    # Step 3: Return the completed dictionary



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
