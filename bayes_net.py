from itertools import product

class BayesNet:

    def __init__(self, ldep=None):  # Why not ldep={}? See footnote 1.
        if not ldep:
            ldep = {}
        self.dependencies = ldep

    # The network data is stored in a dictionary that
    # associates the dependencies to each variable:
    # { v1:deps1, v2:deps2, ... }
    # These dependencies are themselves given
    # by another dictionary that associates conditional
    # probabilities to conjunctions of mother variables:
    # { mothers1:cp1, mothers2:cp2, ... }
    # The conjunctions are frozensets of pairs (mothervar,boolvalue)
    def add(self,var,mothers,prob):
        self.dependencies.setdefault(var,{})[frozenset(mothers)] = prob

    # Joint probability for a given conjunction of
    # all variables of the network
    def jointProb(self,conjunction):
        prob = 1.0
        for (var,val) in conjunction:
            for (mothers,p) in self.dependencies[var].items():
                if mothers.issubset(conjunction):
                    prob*=(p if val else 1-p)
        return prob

    def ancestors(self, v):
        pass

    def conjuncoes(self, v, b, lanc):
        pass

    # xi -> var
    def individualProb(self, var, val):
        variaveis = [k for k in self.dependencies.keys() if k != var]

        return sum([
            self.jointProb( [(var, value)] + conj )
            for conj in self._generate_conjunction(variaveis)
        ])
    
    # o '_' no início de um método como o caso abaixo, por norma indica que, embora o python não defina, este método é público e não deve ser usado fora da classe
    def _generate_conjunction(self, variaveis):
        if len(variaveis) == 1:
            return [ [(variaveis[0], True)], [(variaveis[0], False)] ]

        l = []
        for c in self._generate_conjunction(variaveis[1:]):
            l.append([(variaveis[0], True)] + c)
            l.append([(variaveis[0], False)] + c)

        return l


# Footnote 1:
# Default arguments are evaluated on function definition,
# not on function evaluation.
# This creates surprising behaviour when the default argument is mutable.
# See:
# http://docs.python-guide.org/en/latest/writing/gotchas/#mutable-default-arguments

