import random
def flip_variable(assignment, var):
    assignment[var] = not assignment[var]
def is_clause_satisfied(clause, assignment):
    for literal in clause:
        var = abs(literal)
        if (literal > 0 and assignment[var]) or (literal < 0 and not assignment[var]):
            return True
    return False
def is_formula_satisfied(formula, assignment):
    return all(is_clause_satisfied(clause, assignment) for clause in formula)
def get_unsatisfied_clauses(formula, assignment):
    return [clause for clause in formula if not is_clause_satisfied(clause, assignment)]
def walk_sat(formula, max_flips, p):
    variables = {abs(literal) for clause in formula for literal in clause}
    assignment = {var: random.choice([True, False]) for var in variables}
    for _ in range(max_flips):
        if is_formula_satisfied(formula, assignment):
            return assignment
        unsatisfied_clauses = get_unsatisfied_clauses(formula, assignment)
        clause = random.choice(unsatisfied_clauses)
        if random.random() < p:
            var_to_flip = abs(random.choice(clause))
        else:
            var_to_flip = max(clause, key=lambda literal: sum(
                is_clause_satisfied(clause, {**assignment, abs(literal): not assignment[abs(literal)]})
                for clause in formula
            ))
            var_to_flip = abs(var_to_flip)
        flip_variable(assignment, var_to_flip)
    return None


