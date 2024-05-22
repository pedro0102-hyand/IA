class BackwardChaining:
    def __init__(self,facts,rules):
        self.facts=facts
        self.rules=rules
    def is_fact(self,fact):
        return fact in self.facts
    def prove(self,goal):
        if self.is_fact(goal):
            return True
        for conditions, conclusion in self.rules:
            if conclusion==goal:
                all_conditions_proved=True
                for condition in conditions:
                    if not self.prove(condition):
                        all_condition_proved=False
                        break
                    if all_conditions_proved:
                        self.facts.append(goal)
                        return True
        return False
initial_facts=[]
rules=[]
goal=""
bc=BackwardChaining(initial_facts,rules)
if bc.prove(goal):
    print("Meta provada")
else:
    print("Meta nao provada")
final_facts=bc.facts
for fact in final_facts:
    print(fact)