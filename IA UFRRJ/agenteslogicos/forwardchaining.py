class ForwardChaining:
    def __init__(self,facts,rules):
        self.facts=facts
        self.rules=rules
    def apply_rules(self,rule):
        conditions,conclusion=rule
        if all(condition in self.facts for condition in conditions):
            return conclusion
        return None
    def infer(self):
        new_facts_added=True
        while new_facts_added:
            new_facts_added=False
            for rule in self.rules:
                conclusion=self.apply_rule(rule)
                if conclusion and conclusion not in self.facts:
                    self.facts.append(conclusion)
                    new_facts_added=True
    def get_facts(self):
        return self.facts
initial_facts=[]
rules=[]
fc=ForwardChaining(initial_facts,rules)
fc.infer()
final_facts=fc.get_facts()
for fact in final_facts:
    print(fact)
