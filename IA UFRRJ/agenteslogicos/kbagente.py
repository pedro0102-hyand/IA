KB=[]
t=0
def KB_AGENT(percept):
    global KB,t
    TELL(KB,MAKE_PERCEPT_SENTENCE(percept,t))
    action=ASK(KB,MAKE_ACTION_QUERRY(t))
    TELL(KB,MAKE_ACTION_SENTENCE(action,t))
    t=t+1
    return action
def TELL(KB,sentence):
    KB.append(sentence)
def ASK(KB,query):
    return query(KB)
def MAKE_PERCEPT_SENTENCE(percept,time):
    return(percept,time)
def MAKE_ACTION_QUERRY(time):
    def  query(KB):
        for sentence in KB:
            if sentence[1]==time:
                return sentence[0]
        return None
    return query
def MAKE_ACTION_SENTENCE(action,time):
    return(action,time)
            