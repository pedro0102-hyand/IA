def TT_ENTAILS(KB,alpha):
    symbols=list(set(get_propositional_symbols(KB)+get_propositional_symbols(alpha)))
    return TT_CHECK_ALL(KB,alpha,symbols,{})
def TT_CHECK_ALL(KB,alpha,symbols,model):
    if not symbols:
        if PL_TRUE(KB,model):
            return PL_TRUE(alpha,model)
        else:
            return True
    else :
        P=symbols[0]
        rest=symbols[1:]
        return (TT_CHECK_ALL(KB, alpha, rest, merge(model, {P: True})) and
                TT_CHECK_ALL(KB, alpha, rest, merge(model, {P: False})))
def PL_TRUE(sentence,model):
    pass
def get_propositional_symbols(sentence):
    pass
def merge(dict1,dict2):
    merged=dict1.copy()
    merged.update(dict2)
    return merged