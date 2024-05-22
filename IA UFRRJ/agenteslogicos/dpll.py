def dpll(formula,assignment=None):
    if assignment is None:
        assignment={}
    def is_clause_satisfied(clause):
        for literal in clause:
            var=abs(literal)
            if var in assignment and ((literal>0 and assignment[var]) or(literal<0 and not assignment[var])):
                return True
        return False
    def is_clause_unsatisfied(clause):
        for literal in clause:
            var=abs(literal)
            if var not in assignment:
                return False
            if(literal>0 and not assignment[var]) or(literal<0 and assignment[var]):
                return True
        return False
    def select_unassigned_variable():
        for clause in formula:
            for literal in clause:
                if abs(literal) not in assignment:
                    return abs(literal)
        return None
    simplified_formula=[]
    for clause in formula:
        if is_clause_satisfied(clause):
            continue
        simplified_clause=[literal for literal in clause if abs(literal) not in assignment]
        if not simplified_clause:
            return None
        simplified_formula.append(simplified_clause)
    if not simplified_formula:
        return assignment
    for clause in simplified_formula:
        if is_clause_unsatisfied(clause):
            return None
    var=select_unassigned_variable()
    if var is None:
        return assignment
    for value in [True,False]:
        assignment[var]=value
        result=dpll(simplified_formula,assignment)
        if result is not None:
            return result
        del assignment[var]
    return None