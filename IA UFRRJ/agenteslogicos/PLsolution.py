def PL_RESOLUTION(KB,alpha):
    clauses=CNF_conversion(KB,negate(alpha))
    new=set()
    while True:
        for Ci in clauses:
            for Cj in clauses:
                if Ci != Cj:
                    resolventes=PL_RESOLVE(Ci,Cj)
                    if set() in resolventes:
                        return True
                    new.update(resolventes)
        if new.issubset(clauses):
            return False
        clauses.update(new)
def CNF_conversion(sentece):
    pass
def negate(sentence):
    pass
def PL_RESOLVE(Ci,Cj):
    pass
